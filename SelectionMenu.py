from PyQt6.QtWidgets import QPushButton, QDialog, QLineEdit, QComboBox, QLabel, QGridLayout, QColorDialog, QCheckBox, QSpinBox
from PyQt6.QtCore import Qt
from PIL import ImageFont

class TextDefMenu(QDialog):
    def __init__(self):
        super().__init__()
        
        # Default values
        self.fontsize = 200
        self.title = 'Default'
        self.depth = 50
        
        # Window
        self.window_width, self.window_height = 600, 300
        self.setMinimumSize(self.window_width, self.window_height)
        
        # Create Buttons, ComboBoxes,...
        self.fontLabel = QLabel('Font')  
        self.fontBox = QComboBox()        # Combobox for font
        self.textColorLabel = QLabel('Text Color')  
        self.textColorDialog = QColorDialog()         # Textbox for color
        self.textColorDialog.setFixedWidth(150)
        self.textLabel = QLabel('Text')  
        self.titleTextbox = QLineEdit()         # Textbox for title
        self.titleTextbox.setFixedWidth(150)
        self.fontSizeLabel = QLabel('Font Size')  
        self.sizeSpinbox = QSpinBox()         # Spinbox for size
        self.sizeSpinbox.setRange(1, 1000)   # TODO: adjust range to an appropriate value
        self.sizeSpinbox.setFixedWidth(150)
        self.threeDLabel = QLabel('3D')  
        self.threeDCheckBox = QCheckBox() # Checkbox for 3D Text
        # TODO: Add Textbox for 3D Depth, in case 3D is selected 
        self.button2 = QPushButton('Create text without an image')   # Button to confirm all textboxes
        self.button2.clicked.connect(self.getUserOptions)
          
        # Create grid layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.fontLabel, 0, 0)
        self.layout.addWidget(self.fontBox, 0, 1)
        self.layout.addWidget(self.textColorLabel, 1, 0)
        self.layout.addWidget(self.textColorDialog, 1, 1)
        self.layout.addWidget(self.textLabel, 2, 0)
        self.layout.addWidget(self.titleTextbox, 2, 1)
        self.layout.addWidget(self.fontSizeLabel, 3, 0)
        self.layout.addWidget(self.sizeSpinbox, 3, 1)
        self.layout.addWidget(self.threeDLabel, 4, 0)
        self.layout.addWidget(self.threeDCheckBox, 4, 1)
        self.layout.addWidget(self.button2, 5, 0, 1, 2)  # span two columns for the button
        
        # Set column stretch to push items to the top
        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 1)

        # Set layout
        self.setLayout(self.layout)

        # Show window
        self.show()

    
    def get(self):
        # Parse data
        self.fontsize = int(self.textColorDialog.text())  # TODO: fix
        self.title = str(self.titleTextbox.text())
        self.depth = int(self.sizeSpinbox.text())
        
    
    def getUserOptions(self):
        self.get()
        self.font = ImageFont.truetype("arial.ttf", self.fontsize)  # Specify font file and size
        return self.title, self.fontsize, self.depth

        