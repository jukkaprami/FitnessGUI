# MAIN WINDOW FOR FITNESS APPLICATION
# ===================================

# LIBRARIES AND MODULES
import sys
from PyQt5 import *
from PyQt5 import QtCore # Core functionality of Qt
from PyQt5 import QtWidgets as QW # UI elements functionality
from PyQt5.uic import loadUi
import kuntoilija
import timetools
# TODO: Import some library able to plot trends and make it as widget in the UI

# Class for the main window
class Mainwindow(QW.QMainWindow):

    """MainWindow for the fitness app"""

    # Constructor for the main window
    def __init__(self):
        super().__init__()

    # Load the UI file
        loadUi('main.ui', self)

    # Define UI controls ie buttons and input fields

        self.nameLE = self.findChild(QW.QLineEdit, 'NameLineEdit')
        self.nameLE.textEdited.connect(self.activateCalculatePB)

        self.birthDateE = self.BirthTime
        self.birthDateE.dateChanged.connect(self.activateCalculatePB)
        self.GenderChoose = self.GenderChoose
        self.GenderChoose.currentTextChanged.connect(self.activateCalculatePB)
        self.weighingDateEdit = self.WeighingDate
        
        # Set the weighing date to current date 
        self.weighingDateEdit.setDate(QtCore.QDate.currentDate())
        self.heightSB = self.Height
        self.heightSB.valueChanged.connect(self.activateCalculatePB)
        self.weightSB = self.Weight
        self.weightSB.valueChanged.connect(self.activateCalculatePB)
        self.neckSB = self.Neck
        self.neckSB.valueChanged.connect(self.activateCalculatePB)
        self.waistSB = self.Waist
        self.waistSB.valueChanged.connect(self.activateCalculatePB)
        self.hipSB = self.Hip
        self.hipSB.setEnabled(False)
        self.hipSB = self.hipSB.valueChanged.connect(self.activateCalculatePB)
        
        # TODO: Disable Calculate button until have been edited
        # self.CalculatePB = self.CalculateButton
        self.CalculatePB = self.findChild(QW.QPushButton,'CalculateButton')
        self.CalculatePB.clicked.connect(self.calculateAll)
        self.CalculatePB.setEnabled(False)

        # TODO: Disable Save Button until new values are calculated 
        self.savePB = self.findChild(QW.QPushButton, 'SaveButton')
        self.savePB = self.SaveButton
        self.savePB.clicked.connect(self.saveData)
        self.savePB.setEnabled(False)

    # Define slots ie methods 

    def activateCalculatePB(self):
        self.CalculatePB.setEnabled(True)
        if self.nameLE == '':
            self.CalculatePB.setEnabled(False)

        if self.birthDateE.date() == QtCore.QDate(1900, 1, 1):
            self.CalculatePB.setEnabled(False)

        if self.GenderChoose.currentText() == '':
            self.CalculatePB.setEnabled(False)

        if self.heightSB.value() == 100:
            self.CalculatePB.setEnabled(False)

        if self.weightSB.value() == 20:
            self.CalculatePB.setEnabled(False)

        if self.neckSB.value() == 10:
            self.CalculatePB.setEnabled(False)

        if self.waistSB.value() == 30:
            self.CalculatePB.setEnabled(False)

        if self.GenderChoose.currentText() == 'Nainen':
            self.hipSB.setEnabled (True)
            if self.hipSB.value() == 50:
             self.CalculatePB.setEnable(False)

     # Calculates BMI, Finnish and US fat percentages and updates correspoding labels    

    def calculateAll(self):
        name = self.nameLE.text()
        height = self.heightSB.value()
        weight = self.weightSB.value()
        self.savePB.setEnabled(True)

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

        neck = self.neckSB.value()
        waist = self.waistSB.value()
        hip = self.hipSB.value()

        if age >=18:
            # Create and athelete from kuntoilija class
            athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender)
            bmi = athlete.bmi

        else:
            athelete = kuntoilija.juniorikuntoilija(name, height, weight, age, gender)

        bmi = athlete.bmi
        self.BMILabel.setText(str(bmi))

        label_9 = athelete.rasvaprosentti()

        adultFatPercentange = athlete.rasvaprosentti()

        if gender == 1:
            USAFatPercentange = athlete.usa_rasvaprosentti_mies(height, waist, neck,)
        else:
            USAFatPercentange = athlete.usa_rasvaprosentti_nainen(height, waist, neck, hip)

        self.label_9.setText(str(adultFatPercentange))
        self.label_10.setText(str(USAFatPercentange))

    # TODO: Make this method to save results to disk drive
    # Saves data to disk
    def saveData(self):
        pass
 
if __name__ == "__main__":
    # Create the application
    app = QW.QApplication(sys.argv)

    # Create the Mainwindow(and show it)
    appWindow = Mainwindow()
    appWindow.show()
    sys.exit(app.exec())

    # Start the application 