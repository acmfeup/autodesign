from PyQt6.QtWidgets import QLabel, QDialog
from PyQt6.QtGui import QPixmap

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
        
        
        