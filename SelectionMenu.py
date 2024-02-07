from PyQt6.QtWidgets import QPushButton, QDialog, QLineEdit, QComboBox, QLabel, QGridLayout, QColorDialog, QCheckBox, QSpinBox
from PyQt6.QtGui import QColor, QIcon
import os

class TextDefMenu(QDialog):
    def __init__(self):
        super().__init__()
        
        # Default values
        self.font = 'arial.ttf'
        self.text = 'Default'
        self.fontsize = 100
        self.threeD = False
        self.color = (255, 255, 255)
        self.x = 0
        self.y = 0
        self.userChoices = [self.font, self.text, self.fontsize, self.threeD, self.color]   # user choices to be applied
        
        # Window
        self.window_width, self.window_height = 250, 300
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle("Add Text")
        self.setWindowIcon(QIcon("Resources/Icons/ACM_logo.jpg"))  # Provide the path to your icon image
        
        # Create Buttons, ComboBoxes,...
        self.fontLabel = QLabel('Font')  
        self.fontBox = QComboBox()        # Combobox for font
        self.addFontsToList()
        self.textColorLabel = QLabel('Text Color')  
        self.colorLabel = QLabel('Color')
        self.colorButton = QPushButton()   # Button for picking color
        self.colorButton.clicked.connect(self.color_picker)
        self.textLabel = QLabel('Text')  
        self.titleTextbox = QLineEdit()         # Textbox for title
        self.titleTextbox.setFixedWidth(150)
        self.fontSizeLabel = QLabel('Font Size')  
        self.sizeSpinbox = QSpinBox()         # Spinbox for size
        self.sizeSpinbox.setRange(1, 1000)   # TODO: adjust range to an appropriate value
        self.sizeSpinbox.setValue(50)
        self.sizeSpinbox.setFixedWidth(150)
        self.depthLabel = QLabel('3D Depth')  
        self.depthSpinbox = QSpinBox()         # Spinbox for depth
        self.depthSpinbox.setRange(1, 1000)   # TODO: adjust range to an appropriate value
        self.depthSpinbox.setFixedWidth(150)  
        self.depthSpinbox.setEnabled(False)  
        self.depthSpinbox.setValue(10)
        self.threeDLabel = QLabel('3D')  
        self.threeDCheckBox = QCheckBox() # Checkbox for 3D Text
        self.threeDCheckBox.stateChanged.connect(self.toggleDepthSpinbox)
        self.threeDCheckBox.setChecked(False)  # Set initial state to unchecked
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
        self.layout.addWidget(self.fontLabel, 0, 0)
        self.layout.addWidget(self.fontBox, 0, 1)
        self.layout.addWidget(self.textLabel, 1, 0)
        self.layout.addWidget(self.titleTextbox, 1, 1)
        self.layout.addWidget(self.fontSizeLabel, 2, 0)
        self.layout.addWidget(self.sizeSpinbox, 2, 1)
        self.layout.addWidget(self.threeDLabel, 3, 0)
        self.layout.addWidget(self.threeDCheckBox, 3, 1)
        self.layout.addWidget(self.depthLabel, 3, 2)
        self.layout.addWidget(self.depthSpinbox, 3, 3)
        self.layout.addWidget(self.colorLabel, 4, 0)
        self.layout.addWidget(self.colorButton, 4, 1)
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
    
    def color_picker(self):
        pickedColor = QColorDialog.getColor()
        r, g, b, t = pickedColor.getRgb()
        self.color = (r, g, b) 
        print(self.color)
        if pickedColor.isValid():
            self.colorButton.setStyleSheet(f"background-color: {pickedColor.name()}; color: white;")

    def updateChoices(self):
        self.font = self.fontBox.currentText()  # Get selected font from ComboBox
        self.text = self.titleTextbox.text()    # Get text from QLineEdit
        self.fontsize = self.sizeSpinbox.value()  # Get value from SpinBox
        self.threeD = self.threeDCheckBox.isChecked()  # Get whether CheckBox is checked
        self.depth = self.depthSpinbox.value()
        self.x = self.xSpinbox.value()
        self.y = self.ySpinbox.value()
        self.userChoices = [self.font, self.text, self.fontsize, self.threeD, self.color, self.depth, self.x, self.y]   # tuple of user choices to be applied

    def conclude(self):
        self.updateChoices()
        self.close()
        return self.userChoices
    
    # Define the method to toggle the enabled state of the depthSpinbox
    def toggleDepthSpinbox(self):
        if self.threeDCheckBox.isChecked():
            self.depthSpinbox.setEnabled(True)
        else:
            self.depthSpinbox.setEnabled(False)
            
    def loadLayer(self, layer):
        self.fontBox.setCurrentText(layer[0]) # TODO: fix
        self.titleTextbox.setText(layer[1])
        self.sizeSpinbox.setValue(layer[2])
        self.depthSpinbox.setValue(layer[5])
        self.threeDCheckBox.setChecked(layer[3])
        self.color = layer[4]
        qcolor = QColor(*self.color)
        self.colorButton.setStyleSheet(f"background-color: {qcolor.name()}; color: white;")
        self.xSpinbox.setValue(layer[6])
        self.ySpinbox.setValue(layer[7])
        
    def addFontsToList(self):
        self.fontBox.addItem('arial.ttf')
        self.fontBox.addItem('georgia.ttf')
        
        for file in os.listdir("Custom fonts"):
            filename = os.fsdecode(file)
            if filename.endswith(".ttf"): 
                print('Font found:', filename)
                self.fontBox.addItem(filename)
            else:
                continue