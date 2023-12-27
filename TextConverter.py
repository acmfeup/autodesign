from PyQt6.QtWidgets import QLabel, QDialog
from PyQt6.QtGui import QPixmap
#from PIL import Image, ImageDraw, ImageFont

class TextConverterMenu(QDialog):
    def __init__(self, image_path):
        super().__init__()

        self.window_width, self.window_height = 800, 500
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle("Text Converter")
 
        label = QLabel(self)
        pixmap = QPixmap(image_path)
        label.setPixmap(pixmap)
 
        self.show()
        
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
        
        
        