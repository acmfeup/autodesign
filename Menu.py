from PyQt6.QtWidgets import QWidget, QPushButton, QFileDialog, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QFont
from TextConverter import TextConverterMenu
from PyQt6.QtCore import Qt
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.window_width, self.window_height = 500, 200
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle("Autodesign")
        self.setWindowIcon(QIcon("Resources/Icons/ACM_logo.jpg"))  # Provide the path to your icon image
        
        buttonWidth = 200
        buttonHeight = 50
        buttonFont = 'Tahoma'
        titleFont = buttonFont
        buttonFontSize = 10
        buttonSpacing = 15
        
        # Create widgets
        self.titleLabel = QLabel('Autodesign')
        self.titleLabel.setFont(QFont(titleFont, 50))
        self.importImageButton = QPushButton("Import an image")
        self.importImageButton.setFixedSize(buttonWidth, buttonHeight)
        self.importImageButton.setFont(QFont(buttonFont, buttonFontSize))
        self.importImageButton.pressed.connect(self.importImage)        
        
        # Create Layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.titleLabel, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addSpacing(30) 
        self.layout.addWidget(self.importImageButton, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addSpacing(buttonSpacing) 

        # Set Layout
        self.setLayout(self.layout)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.show()
        
    def importImage(self):
        file_filter = 'Image File (*.png *.jpg)'
        response = QFileDialog.getOpenFileName(
            parent = self,
            caption = 'Select a file',
            directory = os.getcwd(),
            filter = file_filter,
            initialFilter = 'Image File (*.png *.jpg)'
        )
        
        if response[0]:  # Check if a valid file was selected
            self.openTextConverter(response[0])
        else:
            print("Import canceled or invalid file selected.")
        
        
    def openTextConverter(self, image_path):
        textConverter = TextConverterMenu(image_path)
        self.close()
        textConverter.exec()
        