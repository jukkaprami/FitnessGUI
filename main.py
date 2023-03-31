# MAIN WINDOW FOR FITNESS APPLICATION
# ===================================

# LIBRARIES AND MODULES
import sys
from PyQt5 import *
from PyQt5 import QtCore # Core functionality of Qt
from PyQt5 import QtWidgets # UI elements functionality
from PyQt5.uic import loadUi
import kuntoilija
import timetools

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
        
        # Set the weighing date to current date 
        self.weighingDateEdit.setDate(QtCore.QDate.currentDate())
        self.heightSB = self.Height
        self.weightSB = self.Weight
        self.neckSB = self.Neck
        self.waistSB = self.Waist
        self.hipSB = self.Hip
        
        # TODO: Disable Calculate button until have been edited
        self.CalculatePB = self.CalculateButton
        self.CalculatePB.clicked.connect(self.calculateAll)

        self.savePB = self.SaveButton
        self.savePB.clicked.connect(self.saveData)

    # Define slots ie methods 

    # Calculates BMI, Finnish and US fat percentages and updates correspoding labels
    def calculateAll(self):
        name = self.nameLE.text()
        height = self.heightSB.value()
        weight = self.weightSB.value()

        #Convert birthday to ISO string usingIQTCores methods
        birthday = self.birthDateE.date().toString(format=QtCore.Qt.ISODate)

        # Set Gender value according to ComboBox value
        gendertext = self.genderComboBox.currentText()
        if gendertext == 'Mies':
            gender = 1

        else:
            gender = 0

        # Convert weighing data to ISO string
        dateofweighing = self.weighingDateEdit.date().toString(format=QtCore.Qt.ISODate)

        # Calculate time diffrence using your homemade tools
        age = timetools.datediff2(birthday, dateofweighing, 'year')

        # Create and athelete from kuntoilija class
        athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender)
        bmi = athlete.bmi

        self.BMILabel.setText(str(bmi))


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