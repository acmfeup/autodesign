from SelectionMenu import TextDefMenu 
from PyQt6.QtWidgets import QDialog, QGraphicsView, QGraphicsScene, QVBoxLayout, QGraphicsPixmapItem, QSizePolicy, QWidget, QPushButton, QHBoxLayout, QSplitter, QListWidget
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from PIL import Image, ImageDraw, ImageFont

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
        pixmap = QPixmap(image_path)
        item = QGraphicsPixmapItem(pixmap)
        self.graphicsScene.addItem(item)
                
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
        self.drawText(font, text, fontsize, threeD, color, depth, x, y)
        self.setDisabled(False)
        
    def updatePreview(self):
        # Update QGraphicsScene with the modified image
        pixmap = QPixmap(self.image_path)
        item = QGraphicsPixmapItem(pixmap)
        self.graphicsScene.clear()  # Clear existing items in the scene
        self.graphicsScene.addItem(item)

        # Set the new scene to the graphicsView
        self.graphicsView.setScene(self.graphicsScene)
        
        # Update layers 
        self.layersListWidget.clear()
        for layer_item in self.layersList:
            self.layersListWidget.addItem(layer_item[1])  # Only add Text to layers view
        
        
    def onLayersItemClick(self):
        print('layers list before:', self.layersList)
        self.setDisabled(True)
        selected_index = self.layersListWidget.currentRow()
        layerEditor = TextDefMenu()
        layerEditor.loadLayer(self.layersList[selected_index])
        layerEditor.exec()
        subLayer = layerEditor.conclude()   # Layer that will substitute the old one
        self.layersList[selected_index] = subLayer
        print('layers list after:', self.layersList)
        self.updatePreview()
        self.setDisabled(False)
        #self.deleteLayer(0)  # DEBUG
        
    def deleteLayer(self, layerIndex):
        self.layersList.pop(layerIndex)
        self.updatePreview()
        
    def drawText(self, font, text, fontsize, threeD, color, depth, x, y):
        layer_item = [font, text, fontsize, threeD, color, depth, x, y]
        self.addLayer(layer_item, text)
        with Image.open(self.image_path) as im:
            fontPIL = ImageFont.truetype(font, fontsize) 
            draw = ImageDraw.Draw(im)
            text_position = (x, y)  # Position of the text
            if threeD == True:
                for i in range(depth):
                    text_color = (i, i, i)  # RGB color for the text
                    text_position = (x + i, y + i)  # Position of the text
                    draw.text(text_position, text, font=fontPIL, fill=text_color)
            draw.text(text_position, text, font=fontPIL, fill=color)
            im.save("output.png") # TODO: change output path and name
            self.image_path = "output.png"
            self.updatePreview()

    def addLayer(self, layer_item, layer_name):
        self.layersList.append(layer_item)
        self.layersListWidget.addItem(layer_name)
        
