# MAIN WINDOW FOR FITNESS APPLICATION
# ===================================

# LIBRARIES AND MODULES
import sys
from PyQt5 import *
from PyQt5 import QtCore # Core functionality of Qt
from PyQt5 import QtWidgets # UI elements functionality
from PyQt5.uic import loadUi
import kuntoilija

# Class for the main window
class Mainwindow(QtWidgets.QMainWindow):

    """MainWindow for the fitness app"""

    # Constructor for the main window
    def __init__(self):
        super().__init__()

    # Load the UI file
        loadUi('main.ui', self)

    # Define UI controls ie buttons and input fields

        self.nameLE = self.NameLineEdit
        self.birthDateE = self.BirthTime
        self.genderComboBox = self.GenderChoose
        self.weighingDateEdit = self.WeighingDate
        self.weighingDateEdit.setDate(QtCore.QDate.currentDate())
        self.heightSB = self.Height
        self.weightSB = self.Weight
        self.neckSB = self.Neck
        self.waistSB = self.Waist
        self.hipSB = self.Hip
        

        self.CalculatePB = self.CalculateButton
        self.CalculatePB.clicked.connect(self.calculateAll)

        self.savePB = self.SaveButton
        self.savePB.clicked.connect(self.saveData)

    # Define slots ie methods 

    # Calculates BMI, Finnish and US fat percentages and updates correspoding labels
    def calculateAll(self):
        height = self.heightSB.value()
        weight = self.weightSB.value()
        age = 100
        gender = self.genderComboBox.currentText()
        dateofweighing = self.weighingDateEdit.date().toString(format=QtCore.Qt.ISODate)

        # Create and athelete from kuntoilija class
        # athlete = kuntoilija.Kuntoilija()
        # bmi = athlete.bmi

        self.BMILabel.setText(dateofweighing)


    # Saves data to disk
    def saveData(self):
        pass

if __name__ == "__main__":
    # Create the application
    app = QtWidgets.QApplication(sys.argv)

    # Create the Mainwindow(and show it)
    appWindow = Mainwindow()
    appWindow.show()
    sys.exit(app.exec())

    # Start the application 