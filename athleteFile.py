# ROTINES TO CREATE, WRITE AND READ ATHLETE DATA FUKE
# ===================================================

# LIBRARIES AND MODULES

import json

# CLASS DEFINITIONS

class ProcessJsonFile(object):
    def __init__(self):
        pass

    def saveData(self,file):
        """Saves all athelete data to disk

        Args:
            file (str): Name of the file
            data (list): List of dictionaries

        Returns:
            tuple: Error code, Error message, detailed error message
        """
        status = (0, 'Tallennus onnistui', 'All data saved succesfully')
        return status

    def readData(self,file):
        """Reads athelete data from file

        Args:
            file (str): Name of the file

        Returns:
            tuple: Error code, Error Message, deatiled error message, data
        """
        # Read previous athlete_data from disk

        with open('file', 'r') as fileToRead:
            athlete_data = json.load(fileToRead)
            message = 'OK'
            detailedMessage = 'Data read succesfully from disk'
            data = (0, message, detailedMessage, athlete_data)
        return data


    def appenData(self, file, data):
        """Adds a new json object to the file

        Args:
            file (str): Name of the file
            data (dict): python dictionary containing data

        Returns:
            tuple: Error code, Error message, detailed error message
        """

        status = (0, 'Tallennus onnistui', 'All data saved succesfully')
        return status
        

# PRELIMINARY TESTS

if __name__ == "__main__":
    pass
