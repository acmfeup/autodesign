from SelectionMenu import TextDefMenu 
from PyQt6.QtWidgets import QDialog, QGraphicsView, QGraphicsScene, QVBoxLayout, QGraphicsPixmapItem, QSizePolicy, QWidget, QPushButton, QHBoxLayout, QSplitter
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PIL import Image, ImageDraw, ImageFont

class TextConverterMenu(QDialog):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        
        self.image_path = image_path

        self.window_width, self.window_height = 800, 500
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle("Text Converter")
 
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
        button1 = QPushButton("Add 3D text")
        button1.pressed.connect(self.add3dText)
        button2 = QPushButton("Button 2")
        user_menu_layout.addWidget(button1)
        user_menu_layout.addWidget(button2)
        splitter.addWidget(user_menu_widget)
        splitter.setSizes([int(self.window_width * 0.75), int(self.window_width * 0.25)])

        main_layout.addWidget(splitter)

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
            self.openTextDefMenu()
            title, fontsize, depth = 'AAA', 200, 50 # TEMPORARY    
            font = ImageFont.truetype("arial.ttf", fontsize)  # Specify your font file and size
            
            draw = ImageDraw.Draw(im)
            text_position = (0, 0)  # Position of the text
            for i in range(depth):
                text_color = (i, i, i)  # RGB color for the text
                text_position = (0 + i, 10 + i)  # Position of the text
                draw.text(text_position, title, font=font, fill=text_color)
            text_color = (0, 255, 255)
            draw.text(text_position, title, font=font, fill=text_color)
            im.save("output.png")
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
        
    def openTextDefMenu(self):
        pass
        textDefMenu = TextDefMenu()
        textDefMenu.exec()
        
        
        
        