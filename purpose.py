# LABEL FOR THE PURPOSE OF THIS APPLICATION
# =========================================

# LIBRARIES AND MODULES
from PyQt6 import QtWidgets, uic # Elements and a tool to load the UI from ui file
import sys # For accessing system parameters


# CLASS DEFINITIONS

# Class for the main window
class MainWindow(QtWidgets.QMainWindow):

    # Constructor method
    def __init__(self):
        super().__init__()

        # Load the ui file
        uic.loadUi('mainWindow.ui', self)

        # UI OBJECTS

        # Controls
        self.controlName = self.uiFileConntrolName # Direct assignment, the simple way
        self.anotherControlName = self.findChild(QtWidgets.QLineEdit, 'anotherUiFileControlName') # Assignment by pointer for a line edit

        # Indicators
        self.indicatorNamer = self.uiFileIndicatorName
        self.anotherindicatorName = self.findChild(QtWidgets.QLabel , 'uiFileAnotherIndicatorName')

        # SIGNALS
        # Signals are triggered when something happens

        # When a button has been clicked by the user call a method (slot)
        self.controlName.clicked.connect(self.someMethod)  

        # MAKE UI VISIBLE
        self.show() # Ui can be made visible also later in main part of the program

    # SLOTS
    # Methods to execute when the corresponding signal is emitted
    
    def someMethod(self):
        self.indicatorName.setText('Hippopotamus') # Sets the text of label

# CREATE & RUN UI
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) # Create the application
    mainwindow = MainWindow() # Create the ui
    app.exec_() # Start the app