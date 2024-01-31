from SelectionMenu import TextDefMenu 
from PyQt6.QtWidgets import QDialog, QGraphicsView, QGraphicsScene, QVBoxLayout, QGraphicsPixmapItem, QSizePolicy, QWidget, QPushButton, QHBoxLayout, QSplitter
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from PIL import Image, ImageDraw, ImageFont

class TextConverterMenu(QDialog):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        
        self.image_path = image_path

        self.window_width, self.window_height = 800, 500
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle("Autodesign")
        self.setWindowIcon(QIcon("Resources/Icons/ACM_logo.jpg"))  # Provide the path to your icon image
 
        main_layout = QHBoxLayout(self)
        
        # Create a splitter to divide the window into two parts
        splitter = QSplitter(Qt.Orientation.Horizontal)

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
        button3 = QPushButton("Edit Layers")
        button4 = QPushButton("Save Image")

        user_menu_layout.addWidget(button1)
        user_menu_layout.addWidget(button2)
        user_menu_layout.addWidget(button3)
        user_menu_layout.addWidget(button4)

        splitter.addWidget(user_menu_widget)
        splitter.setSizes([int(self.window_width * 0.75), int(self.window_width * 0.25)])

        main_layout.addWidget(splitter)
        
        self.layersList = [] # list that stores all layers

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
        with Image.open(self.image_path) as im:
            self.setDisabled(True)
            textDefMenu = TextDefMenu()
            textDefMenu.exec()
            font, text, fontsize, threeD, color = textDefMenu.get()
            depth = 15 # TODO: depth missing
            
            fontPIL = ImageFont.truetype(font, fontsize) 
            draw = ImageDraw.Draw(im)
            text_position = (0, 0)  # Position of the text
            for i in range(depth):
                text_color = (i, i, i)  # RGB color for the text
                text_position = (0 + i, 10 + i)  # Position of the text
                draw.text(text_position, text, font=fontPIL, fill=text_color)
            #text_color = (0, 255, 255)
            draw.text(text_position, text, font=fontPIL, fill=color)
            im.save("output.png")
            self.image_path = "output.png"
            print("IMAGE SAVED")
            self.updatePreview()
            self.setDisabled(False)
        
    def updatePreview(self):
        # Update QGraphicsScene with the modified image
        pixmap = QPixmap("output.png")
        item = QGraphicsPixmapItem(pixmap)
        self.graphicsScene.clear()  # Clear existing items in the scene
        self.graphicsScene.addItem(item)

        # Set the new scene to the graphicsView
        self.graphicsView.setScene(self.graphicsScene)
        

        
        
        
        