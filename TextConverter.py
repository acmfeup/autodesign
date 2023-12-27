from PyQt6.QtWidgets import QDialog, QGraphicsView, QGraphicsScene, QVBoxLayout, QGraphicsPixmapItem, QSizePolicy
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
#from PIL import Image, ImageDraw, ImageFont

class TextConverterMenu(QDialog):
    def __init__(self, image_path):
        super().__init__()

        self.window_width, self.window_height = 800, 500
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle("Text Converter")
 
        layout = QVBoxLayout(self)

        # Create QGraphicsView and QGraphicsScene
        self.graphicsView = QGraphicsView(self)
        self.graphicsScene = QGraphicsScene(self)
        self.graphicsView.setScene(self.graphicsScene)
        layout.addWidget(self.graphicsView)
        
        # Load the image
        pixmap = QPixmap(image_path)
        item = QGraphicsPixmapItem(pixmap)
        self.graphicsScene.addItem(item)
        
        # Set the view size policy to allow resizing
        self.graphicsView.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Enable scroll bars for zooming
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        # Connect the zoom functionality to the wheel event
        self.graphicsView.wheelEvent = self.zoom
        
        self.show()
        
    def zoom(self, event):
        factor = 1.025
        if event.angleDelta().y() < 0:
            factor = 1.0 / factor

        self.graphicsView.setTransform(self.graphicsView.transform().scale(factor, factor))
        
    #def add3dText():
        # with Image.open("chell.jpg") as im:
        #     px = im.load()
            
        #     fontsize = int(input("fontsize: "))
        #     title = input("title: ")
            
        #     draw = ImageDraw.Draw(im)
        #     font = ImageFont.truetype("arial.ttf", fontsize)  # Specify your font file and size
        #     depth = int(input("depth: "))

        #     text_position = (0, 0)  # Position of the text
        #     a = 0
        #     for i in range(depth):
        #         text_color = (i, i, i)  # RGB color for the text
        #         text_position = (0 + i, 10 + i)  # Position of the text
        #         draw.text(text_position, title, font=font, fill=text_color)
        #         a = i
        #     text_color = (0, 255, 255)
        #     draw.text(text_position, title, font=font, fill=text_color)
            
        #     im.save("output.png")
        
        
        