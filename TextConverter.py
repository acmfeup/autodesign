from SelectionMenu import TextDefMenu 
from LayerMenu import LayerMenu
from PyQt6.QtWidgets import QDialog, QGraphicsView, QGraphicsScene, QVBoxLayout, QGraphicsPixmapItem, QFileDialog, QSizePolicy, QWidget, QPushButton, QHBoxLayout, QSplitter, QListWidget, QMessageBox
from PyQt6.QtGui import QPixmap, QIcon, QKeyEvent, QPainter
from PyQt6.QtCore import Qt
from PIL import Image, ImageDraw, ImageFont
import sys
import os
import textwrap

class TextConverterMenu(QDialog):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        
        self.image_path = image_path

        # Set up window
        self.window_width, self.window_height = 800, 500
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle("Autodesign")
        self.setWindowIcon(QIcon("Resources/Icons/ACM_logo.jpg"))  # Provide the path to your icon image
 
        main_layout = QHBoxLayout(self)
        splitter = QSplitter(Qt.Orientation.Horizontal)   # Splitter to divide the window into two parts

        # Create QGraphicsView and QGraphicsScene
        self.graphicsView = QGraphicsView(self)
        self.graphicsView.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.graphicsView.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        self.graphicsScene = QGraphicsScene(self)
        self.graphicsView.setScene(self.graphicsScene)
        self.graphicsView.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.graphicsView.wheelEvent = self.zoom
        main_layout.addWidget(self.graphicsView)
        
        # Add QGraphicsView to the left side of the splitter
        splitter.addWidget(self.graphicsView)
                
        # Create a user menu on the right side
        user_menu_layout = QVBoxLayout()
        user_menu_widget = QWidget(self)
        user_menu_widget.setLayout(user_menu_layout)
        button1 = QPushButton("Add Text")
        button1.pressed.connect(self.add3dText)
        button2 = QPushButton("Add Image")
        button2.pressed.connect(self.addOverlayImage)
        button4 = QPushButton("Save Image")
        self.layersListWidget = QListWidget()
        self.layersListWidget.setDragEnabled(True)
        self.layersListWidget.itemDoubleClicked.connect(self.onLayersItemClick)

        # Add buttons to layout
        user_menu_layout.addWidget(button1)
        user_menu_layout.addWidget(button2)
        user_menu_layout.addWidget(button4)
        user_menu_layout.addWidget(self.layersListWidget)

        splitter.addWidget(user_menu_widget)
        splitter.setSizes([int(self.window_width * 0.75), int(self.window_width * 0.25)])

        main_layout.addWidget(splitter)
        
        self.layersList = []

        # Load the image
        self.pixmap = QPixmap(image_path)
        self.item = QGraphicsPixmapItem(self.pixmap)
        self.graphicsScene.addItem(self.item)
                
        self.maximized = False
        self.show()
        
    def zoom(self, event):
        factor = 1.025
        if event.angleDelta().y() < 0:
            factor = 1.0 / factor
        self.graphicsView.setTransform(self.graphicsView.transform().scale(factor, factor))
        
    def add3dText(self):
        self.setDisabled(True)
        textDefMenu = TextDefMenu()
        textDefMenu.exec()
        font, text, fontsize, threeD, color, depth, x, y = textDefMenu.conclude()
        layer_item = [font, text, fontsize, threeD, color, depth, x, y]
        self.addLayer(layer_item, layer_item[1]) 
        self.setDisabled(False)
        
    def addOverlayImage(self):
        file_filter = 'Image File (*.png *.jpg)'
        response = QFileDialog.getOpenFileName(
            parent = self,
            caption = 'Select a file',
            directory = os.getcwd(),
            filter = file_filter,
            initialFilter = 'Image File (*.png *.jpg)'
        )
        if response[0]:  # Check if a valid file was selected
            imageLayer = ["isImg", response[0]]
            self.addLayer(imageLayer, "Img")
            self.drawOverlayImage(response[0])
        else:
            print("Import canceled or invalid file selected.")
        
        
        
    def updatePreview(self):
        print("current layerslist: ", self.layersList)
        
        # Remove all items from the scene
        for item in self.graphicsScene.items():
            self.graphicsScene.removeItem(item)
        
        self.drawText()
        self.pixmap = QPixmap('output.png')
        self.item.setPixmap(self.pixmap)
        self.graphicsScene.addItem(self.item)
        self.layersListWidget.clear()
        for layer_item in self.layersList:
            self.layersListWidget.addItem(layer_item[1])  # Only add Text to layers view
        
        
    def onLayersItemClick(self):
        #print('layers list before:', self.layersList)  # DEBUG
        self.setDisabled(True)
        selected_index = self.layersListWidget.currentRow()
        layerEditor = LayerMenu()
        layerEditor.loadLayer(self.layersList[selected_index])
        layerEditor.exec()
        subLayer = layerEditor.conclude()   # Layer that will substitute the old one
        #print(self.layersList[selected_index])
        self.layersList[selected_index] = subLayer
        if (subLayer[1] == ''): # Empty layers should be ignored
            self.layersList.remove(subLayer)
        #print('layers list after:', self.layersList)  # DEBUG
        self.updatePreview()
        self.setDisabled(False)
        
    def deleteLayer(self, layerIndex):
        self.layersList.pop(layerIndex)
        self.updatePreview()
        
    def drawImage(self, layer_item):
        self.drawOverlayImage(layer_item[1])
        # TODO: ...
        
    # TODO: Call this function drawLayer instead of drawImage (loop on each layer and determine which function to call)
    def drawText(self):
        output_path = "output.png" # TODO: make this an option (to choose output file name)
        path = self.image_path
        if (self.layersList == []):
            with Image.open(path) as im:
                im.save(output_path)
            im.close()
        for layer_item in self.layersList:
            if layer_item[0] == "isImg":
                self.drawImage(layer_item)
                continue
            font = layer_item[0]
            text = layer_item[1]
            fontsize = layer_item[2]
            threeD = layer_item[3]
            color = layer_item[4]
            depth = layer_item[5]
            x = layer_item[6]
            y = layer_item[7]
            wrapped_text = textwrap.fill(text, width=20)  # Adjust the width as needed
            with Image.open(path) as im:
                fontPIL = ImageFont.truetype('./Custom fonts/'+ font, fontsize)
                draw = ImageDraw.Draw(im)
                text_position = (x, y)  # Position of the text
                if threeD == True:
                    for i in range(depth):
                        text_color = (i, i, i)  # RGB color for the text
                        text_position = (x + i, y + i)  # Position of the text
                        draw.text(text_position, wrapped_text, font=fontPIL, fill=text_color)
                draw.text(text_position, wrapped_text, font=fontPIL, fill=color)
                im.save(output_path) 
            im.close()
            path = output_path

    def drawOverlayImage(self, img_path):
        overlay_pixmap = QPixmap(img_path)
        overlay_item = QGraphicsPixmapItem(overlay_pixmap)
        overlay_item.setOffset(0, 0)
        self.graphicsScene.addItem(overlay_item)    
    
    def addLayer(self, layer_item, layer_name):
        self.layersList.append(layer_item)
        self.layersListWidget.addItem(layer_name)
        self.updatePreview()
        
    def closeEvent(self, event):
        close = QMessageBox()
        close.setWindowTitle("Close program")
        close.setWindowIcon(QIcon("Resources/Icons/ACM_logo.jpg"))  # Set the window icon
        close.setText("Are you sure?")
        close.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        close = close.exec()

        if close == QMessageBox.StandardButton.Yes:
            event.accept()
            sys.exit()
        else:
            event.ignore()
        
    # TODO: Tell user to press F for full screen
    def keyPressEvent(self,event: QKeyEvent):
        k = event.key()
        txt = event.text()
        alt_modifier = (event.modifiers() == Qt.KeyboardModifier.AltModifier)
        if (txt == "f"):
            if (not self.maximized):
                self.maximized = True
                self.showMaximized()
            else:
                self.maximized = False
                self.showNormal()
