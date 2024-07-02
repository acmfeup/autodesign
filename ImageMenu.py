from PyQt6.QtWidgets import QPushButton, QDialog, QLineEdit, QComboBox, QLabel, QGridLayout, QColorDialog, QCheckBox, QSpinBox
from PyQt6.QtGui import QColor, QIcon
import os

class ImgDefMenu(QDialog):
    def __init__(self):
        super().__init__()
        
        # Default values
        self.x = 0
        self.y = 0
        self.userChoices = ["isImg", "no path", self.x, self.y]   # user choices to be applied
        
        # Window
        self.window_width, self.window_height = 250, 300
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle("Edit Overlay Image")
        self.setWindowIcon(QIcon("Resources/Icons/ACM_logo.jpg"))  # Provide the path to your icon image
        
        # Create Buttons, ComboBoxes,...
        self.applyButton = QPushButton('Apply')   # Button to confirm all textboxes
        self.applyButton.clicked.connect(self.conclude)
        self.xLabel = QLabel('x')  
        self.xSpinbox = QSpinBox()         # Spinbox for size
        self.xSpinbox.setRange(1, 1000)   # TODO: adjust range to an appropriate value
        self.xSpinbox.setFixedWidth(150)
        self.yLabel = QLabel('y')  
        self.ySpinbox = QSpinBox()         # Spinbox for size
        self.ySpinbox.setRange(1, 1000)   # TODO: adjust range to an appropriate value
        self.ySpinbox.setFixedWidth(150)
          
        # Create grid layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.xLabel, 5, 0)
        self.layout.addWidget(self.xSpinbox, 5, 1)
        self.layout.addWidget(self.yLabel, 5, 2)
        self.layout.addWidget(self.ySpinbox, 5, 3)
        self.layout.addWidget(self.applyButton, 6, 0, 1, 2)  # span two columns for the button

        # Set column stretch to push items to the top
        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 1)

        # Set layout
        self.setLayout(self.layout)

        # Show window
        self.show()

    def updateChoices(self):
        self.x = self.xSpinbox.value()
        self.y = self.ySpinbox.value()
        self.userChoices = [self.x, self.y]   # tuple of user choices to be applied

    def conclude(self):
        self.updateChoices()
        self.close()
        return self.userChoices
            
    def loadLayer(self, layer):
        self.xSpinbox.setValue(layer[2])
        self.ySpinbox.setValue(layer[3])
        