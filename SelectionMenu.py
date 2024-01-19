from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QDialog, QLineEdit
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PIL import Image, ImageDraw, ImageFont

class TextDefMenu(QDialog):
    def __init__(self):
        super().__init__()
        
        # Default values
        self.fontsize = 200
        self.title = 'Default'
        self.depth = 50
        
        # Window
        self.window_width, self.window_height = 800, 500
        self.setMinimumSize(self.window_width, self.window_height)
        
        # General Layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Textbox for fontsize
        self.input1 = QLineEdit()
        self.input1.setFixedWidth(150)
        layout.addWidget(self.input1)
        # Textbox for title
        self.input2 = QLineEdit()
        self.input2.setFixedWidth(150)
        layout.addWidget(self.input2)
        # Textbox for depth
        self.input3 = QLineEdit()
        self.input3.setFixedWidth(150)
        layout.addWidget(self.input3)
        
        # Button to confirm all textboxes
        button2 = QPushButton("Create text without an image")
        button2.clicked.connect(self.getUserOptions)
        layout.addWidget(button2)

        # Show window
        self.show()
    
    def get(self):
        # Parse data
        self.fontsize = int(self.input1.text())
        self.title = str(self.input2.text())
        self.depth = int(self.input3.text())
    
    def getUserOptions(self):
        self.get()
        self.font = ImageFont.truetype("arial.ttf", self.fontsize)  # Specify font file and size
        return self.title, self.fontsize, self.depth

        