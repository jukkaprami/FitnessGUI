# Form implementation generated from reading ui file 'c:\Users\ADM.STARASOFT\Documents\GitHub\FitnessGUI\main.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1138, 930)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.NameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.NameLineEdit.setGeometry(QtCore.QRect(0, 20, 521, 22))
        self.NameLineEdit.setToolTipDuration(-3)
        self.NameLineEdit.setObjectName("NameLineEdit")
        self.NameLabel = QtWidgets.QLabel(self.centralwidget)
        self.NameLabel.setGeometry(QtCore.QRect(10, 0, 49, 16))
        self.NameLabel.setObjectName("NameLabel")
        self.WeighingDate = QtWidgets.QDateEdit(self.centralwidget)
        self.WeighingDate.setGeometry(QtCore.QRect(550, 20, 110, 22))
        self.WeighingDate.setObjectName("WeighingDate")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 0, 131, 16))
        self.label.setObjectName("label")
        self.Height = QtWidgets.QSpinBox(self.centralwidget)
        self.Height.setGeometry(QtCore.QRect(0, 80, 101, 22))
        self.Height.setObjectName("Height")
        self.Weight = QtWidgets.QSpinBox(self.centralwidget)
        self.Weight.setGeometry(QtCore.QRect(120, 80, 91, 22))
        self.Weight.setObjectName("Weight")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 49, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 60, 49, 16))
        self.label_3.setObjectName("label_3")
        self.Neck = QtWidgets.QSpinBox(self.centralwidget)
        self.Neck.setGeometry(QtCore.QRect(230, 80, 71, 22))
        self.Neck.setObjectName("Neck")
        self.Waist = QtWidgets.QSpinBox(self.centralwidget)
        self.Waist.setGeometry(QtCore.QRect(330, 80, 61, 22))
        self.Waist.setObjectName("Waist")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 60, 49, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 60, 49, 16))
        self.label_5.setObjectName("label_5")
        self.Pelvis = QtWidgets.QSpinBox(self.centralwidget)
        self.Pelvis.setGeometry(QtCore.QRect(430, 80, 61, 22))
        self.Pelvis.setObjectName("Pelvis")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 60, 49, 16))
        self.label_6.setObjectName("label_6")
        self.CalculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.CalculateButton.setGeometry(QtCore.QRect(550, 80, 75, 24))
        self.CalculateButton.setObjectName("CalculateButton")
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(650, 80, 75, 24))
        self.SaveButton.setObjectName("SaveButton")
        self.BirthTime = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.BirthTime.setGeometry(QtCore.QRect(690, 20, 194, 22))
        self.BirthTime.setObjectName("BirthTime")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(690, 0, 131, 16))
        self.label_7.setObjectName("label_7")
        self.BMILabel = QtWidgets.QLabel(self.centralwidget)
        self.BMILabel.setGeometry(QtCore.QRect(10, 160, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BMILabel.setFont(font)
        self.BMILabel.setObjectName("BMILabel")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 210, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(360, 210, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 140, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.GenderChoose = QtWidgets.QComboBox(self.centralwidget)
        self.GenderChoose.setGeometry(QtCore.QRect(910, 20, 151, 22))
        self.GenderChoose.setObjectName("GenderChoose")
        self.FiFatLabel = QtWidgets.QLabel(self.centralwidget)
        self.FiFatLabel.setGeometry(QtCore.QRect(10, 240, 141, 16))
        self.FiFatLabel.setObjectName("FiFatLabel")
        self.UsaFatLabel = QtWidgets.QLabel(self.centralwidget)
        self.UsaFatLabel.setGeometry(QtCore.QRect(360, 240, 121, 16))
        self.UsaFatLabel.setObjectName("UsaFatLabel")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(920, 0, 61, 16))
        self.label_14.setObjectName("label_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1138, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.NameLineEdit.setToolTip(_translate("MainWindow", "Syötä tähän oma nimesi"))
        self.NameLabel.setText(_translate("MainWindow", "Nimi"))
        self.label.setText(_translate("MainWindow", "Punnituspäivä"))
        self.label_2.setText(_translate("MainWindow", "Pituus"))
        self.label_3.setText(_translate("MainWindow", "Paino"))
        self.label_4.setText(_translate("MainWindow", "Kaula"))
        self.label_5.setText(_translate("MainWindow", "Vyötärö"))
        self.label_6.setText(_translate("MainWindow", "Lantio"))
        self.CalculateButton.setText(_translate("MainWindow", "Laske"))
        self.SaveButton.setText(_translate("MainWindow", "Tallenna"))
        self.label_7.setText(_translate("MainWindow", "Syntymäaika"))
        self.BMILabel.setText(_translate("MainWindow", "Painoindeksi"))
        self.label_9.setText(_translate("MainWindow", "Rasvaprosentti (FI)"))
        self.label_10.setText(_translate("MainWindow", "Rasvaprosentti (USA)"))
        self.label_11.setText(_translate("MainWindow", "Painoindeksi"))
        self.GenderChoose.setPlaceholderText(_translate("MainWindow", "Valitse sukupuoli"))
        self.FiFatLabel.setText(_translate("MainWindow", "Rasvaprosentti (FI)"))
        self.UsaFatLabel.setText(_translate("MainWindow", "Rasvaprosentti (USA)"))
        self.label_14.setText(_translate("MainWindow", "Sukupuoli"))
