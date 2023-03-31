...

import os # Needed for path manipulation
from PyQt6.QtGui import QPixmap # To create pixmaps from picture files

...

# Class for the main window
class MainWindow(QtWidgets.QMainWindow):

    # Constructor method
    def __init__(self):
        super().__init__()

        # Load the ui file
        uic.loadUi('mainWindow.ui', self)

...
    

    # A method to open a picture from user's Pictures folder and show it on a label
def openPicture(self):
        relativeWorkingDirectory = '\Pictures' # relative path to user's Pictures folder

        # Get users profile path and join it with Pictures folder's path ~ refers to users profile
        userProfilePath = os.path.expanduser('~')
        workingDirectory = userProfilePath + relativeWorkingDirectory
        
        # Open a file dialog and save name of the chosen file to a variable fileName
        fileName, check = QtWidgets.QFileDialog.getOpenFileName(None, 'Valitse kuva', workingDirectory, 'Kuvatiedostot (*.jpg *.png)')

        # If reading of the file is successful make a pixmap of the file and show it on a label 
        if fileName:

            # Convert the picture file to a pixmap
            picture = QPixmap(fileName)
            self.pictureLabel.setPixmap(picture) # Put the pixmap to the Label element pictureLabel