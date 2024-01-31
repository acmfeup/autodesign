from PyQt6.QtWidgets import QPushButton, QDialog, QLineEdit, QComboBox, QLabel, QGridLayout, QColorDialog, QCheckBox, QSpinBox
from PyQt6.QtGui import QColor, QIcon
from PIL import ImageFont

class TextDefMenu(QDialog):
    def __init__(self):
        super().__init__()
        
        # Default values
        self.font = "arial.ttf"
        self.text = 'Default'
        self.fontsize = 100
        self.threeD = False
        self.color = (0, 0, 0)
        self.updateUserChoices()
        self.userChoices = (self.font, self.text, self.fontsize, self.threeD, self.color)   # tuple of user choices to be applied
        
        # Window
        self.window_width, self.window_height = 250, 300
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle("Add Text")
        self.setWindowIcon(QIcon("Resources/Icons/ACM_logo.jpg"))  # Provide the path to your icon image
        
        # Create Buttons, ComboBoxes,...
        self.fontLabel = QLabel('Font')  
        self.fontBox = QComboBox()        # Combobox for font
        self.textColorLabel = QLabel('Text Color')  
        #color = QColor(0, 0, 0)    # TODO: use in output
        self.colorLabel = QLabel('Color')
        self.colorButton = QPushButton()   # Button for picking color
        self.colorButton.clicked.connect(self.color_picker)
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
        self.applyButton = QPushButton('Apply')   # Button to confirm all textboxes
        self.applyButton.clicked.connect(self.get)
          
        # Create grid layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.fontLabel, 0, 0)
        self.layout.addWidget(self.fontBox, 0, 1)
        self.layout.addWidget(self.textLabel, 1, 0)
        self.layout.addWidget(self.titleTextbox, 1, 1)
        self.layout.addWidget(self.fontSizeLabel, 2, 0)
        self.layout.addWidget(self.sizeSpinbox, 2, 1)
        self.layout.addWidget(self.threeDLabel, 3, 0)
        self.layout.addWidget(self.threeDCheckBox, 3, 1)
        self.layout.addWidget(self.colorLabel, 4, 0)
        self.layout.addWidget(self.colorButton, 4, 1)
        self.layout.addWidget(self.applyButton, 5, 0, 1, 2)  # span two columns for the button
        
        # Set column stretch to push items to the top
        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 1)

        # Set layout
        self.setLayout(self.layout)

        # Show window
        self.show()
    
    def color_picker(self):
        pickedColor = QColorDialog.getColor()
        r, g, b, t = pickedColor.getRgb()
        self.color = (r, g, b) 
        print(self.color)
        if pickedColor.isValid():
            self.colorButton.setStyleSheet(f"background-color: {pickedColor.name()}; color: white;")
    
    def updateUserChoices(self):
        self.userChoices = (self.font, self.text, self.fontsize, self.threeD, self.color)   # tuple of user choices to be applied

    def get(self):
        #self.font = self.fontBox.currentText()  # Get selected font from ComboBox
        self.text = self.titleTextbox.text()    # Get text from QLineEdit
        self.fontsize = self.sizeSpinbox.value()  # Get value from SpinBox
        self.threeD = self.threeDCheckBox.isChecked()  # Get whether CheckBox is checked
        
        self.updateUserChoices()
        self.close()
        return self.userChoices
        