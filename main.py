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
import ohje
import BGPictures # Compiled resources for background images

# TODO: Make another resource file for the help window, build it and import it
# TODO: Import some library able to plot trends and make it as widget in the UI

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

        # TODO: Change spin boxes to sliders adn add labels to show values 
        self.heightSB = self.heightSpinBox
        self.heightSB.valueChanged.connect(self.activateCalculatePB)
        self.weightSB = self.weightSpinBox
        self.weightSB.valueChanged.connect(self.activateCalculatePB)
        self.neckSB =  self.neckSpinBox
        self.neckSB.valueChanged.connect(self.activateCalculatePB)
        self.waistSB = self.waistSpinBox
        self.waistSB.valueChanged.connect(self.activateCalculatePB)
        self.hipsSB = self.hipsSpinBox
        self.hipsSB.valueChanged.connect(self.activateCalculatePB)

        # Background image for body dimensions is a QFrame with a background image by default a woman
        self.dimensionBox = self.dimensionFrame
        

        # Create a status bar for showing informational messages
        self.statusBar = QW.QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.show()
        
        # self.calculatePB = self.calculatePushButton
        self.calculatePB = self.findChild(QW.QPushButton, 'calculatePushButton')
        self.calculatePB.clicked.connect(self.calculateAll)
        self.calculatePB.setEnabled(False)

        # Temporary push button for inserting test values into controls
        # self.testPB = self.testUiPushButton
        # self.testPB.clicked.connect(self.insertTestValues)

        # A push button for savig user data
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
        
        # MENU ACTIONS
        self.actionPalauta_oletukset.triggered.connect(self.restoreDefaults)
        self.actionOhje.triggered.connect(self.openHelpDialog)

        # Read previous athlete_data from disk


    # Define slots ie methods

    # Create a alerting method
    def alert(self, windowTitle, message, detailedMessage):
        msgBox = QW.QMessageBox()
        msgBox.setIcon(QW.QMessageBox.Critical)
        msgBox.setWindowTitle(windowTitle)
        msgBox.setText(message)
        msgBox.setDetailedText(detailedMessage)
        msgBox.exec()

    def warn(self, windowTitle, message, detailedMessage):
        msgBox = QW.QMessageBox()
        msgBox.setIcon(QW.QMessageBox.Warning)
        msgBox.setWindowTitle(windowTitle)
        msgBox.setText(message)
        msgBox.setDetailedText(detailedMessage)
        msgBox.exec()

    def inform(self, windowTitle, message, detailedMessage):
        msgBox = QW.QMessageBox()
        msgBox.setIcon(QW.QMessageBox.Information)
        msgBox.setWindowTitle(windowTitle)
        msgBox.setText(message)
        msgBox.setDetailedText(detailedMessage)
        msgBox.exec()

    def showMessageBox(self, windowTitle, message, detailedMessage, icon='Information'):
        """Creates a message box for various types of messages

        Args:
            windowTitle (str): Header for the message window
            message (str): Message to be shown
            detailedMessage (str): A message that can be shown by pressing details button
            icon (str, optional):  Allowed values: NoIcon, Information, Question, Warning and Critical
            Defaults to Information.
        """
        iconTypes = {'Information': QW.QMessageBox.Information, 'NoIcon': QW.QMessageBox.NoIcon,
         'Question': QW.QMessageBox.Question, 'Warning': QW.QMessageBox.Warning ,
         'Critical': QW.QMessageBox.Critical}
        msgBox = QW.QMessageBox()
        msgBox.setIcon(iconTypes[icon])
        msgBox.setWindowTitle(windowTitle)
        msgBox.setText(message)
        msgBox.setDetailedText(detailedMessage)
        msgBox.exec()
    
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

        if self.genderCB.currentText() == 'Nainen' or self.genderCB.currentText() == '':
            self.hipsSB.show() # Show Hips spinbox
            self.dimensionBox.setStyleSheet("background-image : url(NaisSlice.png)") # Change the bg image

            if self.hipsSB.value() == 50:
                self.calculatePB.setEnabled(False)
        else:
            self.hipsSB.hide() # Hide Hips spinbox
            self.dimensionBox.setStyleSheet("background-image : url(MiesSlice.png)") # Change the bg image

    def insertTestValues(self):
        # Set test values to all controls
        self.nameLE.setText('Teppo Testi')
        testBirthDay = QtCore.QDate(1999, 12, 31)
        self.birthDateE.setDate(testBirthDay)
        self.genderCB.setCurrentText('Mies')
        self.heightSB.setValue(171)
        self.weightSB.setValue(75)
        self.neckSB.setValue(30)
        self.waistSB.setValue(90)
        
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
        if neck < 21:
            #self.alert('Tarkista kaulan koko', 'Kaulan ympärys liian pieni', 'Kaulan koko voi olla välillä 21 - 60 cm')
            self.showMessageBox('Tarkista kaulan koko', 'Kaulan ympärys virheellinen', 'Sallitut arvot 21 - 60 cm', 'Warning')
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

        # Add current values to a list
        self.dataList.append(self.dataRow)

        # Save list to a json file
        jsonfile2 = athleteFile.ProcessJsonFile()
        status = jsonfile2.saveData('athleteData.json', self.dataList)

        # Show message about status of saving on statusbar
        self.statusBar.showMessage(status[1], 4000)

        # TODO: Call error message box if error code is not 0
        if status[0] != 0:
            self.alert(status[1], status[2])
        else:    
            # Set all inputs to their default values
            self.restoreDefaults()

    def restoreDefaults(self):
        # Set all inputs to their default values
        self.nameLE.clear()
        zeroDate = QtCore.QDate(1900, 1, 1)
        self.birthDateE.setDate(zeroDate)
        self.heightSB.setValue(100)
        self.weightSB.setValue(20)
        self.neckSB.setValue(10)
        self.waistSB.setValue(30)
        self.hipsSB.setValue(50)
        self.savePB.setEnabled(False)

    def openHelpDialog(self):
        openHelp = ohje.OpenHelp()
        openHelp.exec()

if __name__ == "__main__":
    # Create the application
    app = QW.QApplication(sys.argv)
    app.setStyle('Fusion') # Use fusion style

    # Create the Main Window object from MainWindow class and show it on the screen
    appWindow = MainWindow()
    appWindow.show()
    sys.exit(app.exec())
    
