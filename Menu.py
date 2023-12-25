from PyQt6.QtWidgets import QWidget, QPushButton, QFileDialog, QTextEdit, QVBoxLayout
from TextConverter import TextConverterMenu
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.window_width, self.window_height = 800, 500
        self.setMinimumSize(self.window_width, self.window_height)
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        button = QPushButton("Import an image")
        button.pressed.connect(self.importImage)
        layout.addWidget(button)
        
        button2 = QPushButton("Create text without an image")
        #button2.pressed.connect(self.openTextConverter())
        layout.addWidget(button2)

        self.textbox = QTextEdit()
        layout.addWidget(self.textbox)
        
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
            self.textbox.setText(str(response))
            self.openTextConverter(response[0])
        else:
            print("Import canceled or invalid file selected.")
            self.textbox.setText("Invalid file")
        
        
    def openTextConverter(self, image_path):
        textConverter = TextConverterMenu(image_path)
        self.close()
        textConverter.exec()
        
        
    
