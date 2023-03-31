# MAIN WINDOW FOR FITNESS APPLICATION
# ===================================

# LIBRARIES AND MODULES
import sys
from PyQt5 import *
from PyQt5 import QtCore # Core functionality of Qt
from PyQt5 import QtWidgets # UI elements functionality
from PyQt5.uic import loadUi

# Class for the main window
class Mainwindow(QtWidgets.QMainWindow):

    """MainWindow for the fitness app"""

    # Constructor for the main window
    def __init__(self):
        super().__init__()

    # Load the UI file
        loadUi('main.ui', self)

    # Define UI controls ie buttons and input fields
        self.CalculatePB = self.CalculateButton
        self.CalculatePB.clicked.connect(self.calculateAll)

    # Define slots ie methods 
    def calculateAll(self):
        self.bmilabel.setvalue('100')

if __name__ == "__main__":
    # Create the application
    app = QtWidgets.QApplication(sys.argv)

    # Create the Mainwindow(and show it)
    appWindow = Mainwindow()
    appWindow.show()
    sys.exit(app.exec())

    # Start the application 