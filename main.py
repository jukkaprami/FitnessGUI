# MAIN WINDOW FOR FITNESS APPLICATION
# ===================================

# LIBRARIES AND MODULES
import sys # For system arguments if needed to run the app
from PyQt5 import QtCore # Core functionality of Qt
from PyQt5 import QtWidgets as QW # UI elements functionality
from PyQt5.uic import loadUi # Reads the UI file
import kuntoilija # Home brew module for athlete objects
import timetools # DIY module for date and time calculations
import athleteFile # Home made module for processing data files


# Class for the main window
class MainWindow(QW.QMainWindow):

    """MainWindow for the fitness app"""

    # Constructor for the main window
    def __init__(self):
        super().__init__()

        # Load the UI file
        loadUi('main.ui', self)

        # Define UI Controls ie buttons and input fields
        self.nameLE = self.findChild(QW.QLineEdit, 'nameLineEdit')
        self.nameLE.textEdited.connect(self.activateCalculatePB)

        self.birthDateE = self.birthDateEdit
        self.birthDateE.dateChanged.connect(self.activateCalculatePB)
        self.genderCB = self.genderComboBox
        self.genderCB.currentTextChanged.connect(self.activateCalculatePB)
        self.weighingDateE = self.weighingDateEdit

        # Set the weighing date to the current date
        self.weighingDateE.setDate(QtCore.QDate.currentDate()) 

        self.heightSB = self.heightSpinBox
        self.heightSB.valueChanged.connect(self.activateCalculatePB)
        self.weightSB = self.weightSpinBox
        self.weightSB.valueChanged.connect(self.activateCalculatePB)
        self.neckSB =  self.neckSpinBox
        self.neckSB.valueChanged.connect(self.activateCalculatePB)
        self.waistSB = self.waistSpinBox
        self.waistSB.valueChanged.connect(self.activateCalculatePB)
        self.hipsSB = self.hipsSpinBox
        self.hipsSB.setEnabled(False)
        self.hipsSB.valueChanged.connect(self.activateCalculatePB)
        
        # TODO: Disable Calculate button until values have been edited
        # self.calculatePB = self.calculatePushButton
        self.calculatePB = self.findChild(QW.QPushButton, 'calculatePushButton')
        self.calculatePB.clicked.connect(self.calculateAll)
        self.calculatePB.setEnabled(False)

        # TODO: Disable Save button until new values are calculated
        # self.savePB = self.savePushButton
        self.savePB = self.findChild(QW.QPushButton, 'savePushButton')
        self.savePB.clicked.connect(self.saveData)
        self.savePB.setEnabled(False)

        # Read data from file and save it to a list
        self.dataList = []
        jsonFile = athleteFile.ProcessJsonFile()
        try:
            data = jsonFile.readData('athleteData.json')
            self.dataList = data[3]
        except Exception as e:
            data = (1, 'Error', str(e), self.dataList)
        
        

        # Read previous athlete_data from disk


    # Define slots ie methods

    
    def activateCalculatePB(self):
        self.calculatePB.setEnabled(True)
        if self.nameLE.text() == '':
            self.calculatePB.setEnabled(False)

        if self.birthDateE.date() == QtCore.QDate(1900, 1, 1):
            self.calculatePB.setEnabled(False)
        
        if self.genderCB.currentText() == '':
            self.calculatePB.setEnabled(False)

        if self.heightSB.value() == 100:
            self.calculatePB.setEnabled(False)

        if self.weightSB.value() == 20:
            self.calculatePB.setEnabled(False)

        if self.neckSB.value() == 10:
            self.calculatePB.setEnabled(False)

        if self.waistSB.value() == 30:
            self.calculatePB.setEnabled(False)

        if self.genderCB.currentText() == 'Nainen':
            self.hipsSB.setEnabled(True)

            if self.hipsSB.value() == 50:
                self.calculatePB.setEnabled(False)
        else:
            self.hipsSB.setEnabled(False)


    # Calculates BMI, Finnish and US fat percentages and updates corresponding labels
    def calculateAll(self):
        name = self.nameLE.text()
        height = self.heightSB.value() # Spinbox value as an integer
        weight = self.weightSB.value()
        self.calculatePB.setEnabled(False)
        self.savePB.setEnabled(True)

        #  Convert birthday to ISO string using QtCore's methods
        birthday = self.birthDateE.date().toString(format=QtCore.Qt.ISODate)
        
        # Set Gender Value according to Combobox value
        gendertext = self.genderCB.currentText()
        if gendertext == 'Mies':
            gender = 1

        else:
            gender = 0

        # Convert Weighing day to ISO string    
        dateOfWeighing = self.weighingDateE.date().toString(format=QtCore.Qt.ISODate)
        
        # Calculate time difference using our home made tools
        age = timetools.datediff2(birthday, dateOfWeighing, 'year')
        neck = self.neckSB.value()
        waist = self.waistSB.value()
        hips = self.hipsSB.value()

        athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender, neck, waist, hips, dateOfWeighing)
        
        bmi = athlete.bmi
        self.bmiLabel.setText(str(bmi))

        fiFatPercentage = athlete.fi_rasva
        usaFatPercentage = athlete.usa_rasva
        
        # Set fat percentage labels
        self.fatFiLabel.setText(str(fiFatPercentage))
        self.fatUsLabel.setText(str(usaFatPercentage))

        self.dataRow = self.constructData(athlete)
        print(self.dataRow)

    def constructData(self, athlete):
        # A dictionary for single weighing of an athlete
        athlete_data_row = {'nimi': athlete.nimi, 'pituus': athlete.pituus, 'paino': athlete.paino,
                'ika': athlete.ika, 'sukupuoli': athlete.sukupuoli, 'pvm': athlete.punnitus_paiva,
                'bmi': athlete.bmi, 'rasvaprosenttiFi': athlete.fi_rasva, 'rasvaprosenttiUs': athlete.usa_rasva
                }
        return athlete_data_row
    
    # Saves data to disk
    def saveData(self):
        self.dataList.append(self.dataRow)
        jsonfile2 = athleteFile.ProcessJsonFile()
        status = jsonfile2.saveData('athleteData.json', self.dataList)
        self.nameLE.clear()
        zeroDate = QtCore.QDate(1900, 1, 1)
        self.birthDateE.setDate(zeroDate)
        self.heightSB.setValue(100)
        self.weightSB.setValue(20)
        self.neckSB.setValue(10)
        self.waistSB.setValue(30)
        self.hipsSB.setValue(50)
        self.savePB.setEnabled(False)

if __name__ == "__main__":
    # Create the application
    app = QW.QApplication(sys.argv)

    # Create the Main Window object from MainWindow class and show it on the screen
    appWindow = MainWindow()
    appWindow.show()
    sys.exit(app.exec())
    
