# MODULE FOR ASKING QUESTIONS FROM CONSOLE AND CONVERTING ANSWERS TO VARIOUS DATA TYPES
# -------------------------------------------------------------------------------------

# LIBRARIES AND MODULES

# CLASS DEFINITIONS

class Question():
    """A class containing methods to ask questions on console
      and converting answers to various datatypes
    ."""

    def __init__(self, question):
        self.question = question

    # A static method to ask a question and convert the answer to an integer without creating an object
    @staticmethod
    def ask_user_integer(question, loop):
        """Asks a question and converts the answer to an integer

        Args:
            loop (bool): If True asks the question until able to convert it

        Returns:
            tuple: answer as integer, error message, error code, detailed error
        """

        # If loop argument is true use while loop until user inputs correct value
        if loop == True:

            while True:
                answer_txt = input(question)

                # Let's try to convert input to numeric
                try:
                    answer = int(answer_txt)
                    result = (answer, 'OK', 0, 'Conversion successful')
                    break

                # If an error occurs tell the user to check
                except Exception as e:
                    print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
                    result = (0, 'Error', 1, str(e))

        # Else ask once and return zero value and error information
        else:
            answer_txt = input(question)

            # Let's try to convert input to numeric
            try:
                answer = int(answer_txt)
                result = (answer, 'OK', 0, 'Conversion successful')

            # If an error occurs tell the user to check
            except Exception as e:
                print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
                result = (0, 'Error', 1, str(e))

        return result

    # A static method to ask a question and convert the answer to a float without creating an object
    @staticmethod
    def ask_user_float(question, loop):
        """Asks a question and converts the answer to a floating point number

        Args:
            question (str): Question to ask
            loop (bool): If True asks the question until able to convert it

        Returns:
            tuple: answer as float, error message, error code, detailed error
        """

        # If loop argument is true use while loop until user inputs correct value
        if loop == True:

            while True:
                answer_txt = input(question)
                
                try:
                    answer_txt = answer_txt.replace(',', '.')
                    answer = float(answer_txt)
                    result = (answer, 'OK', 0, 'Conversion successful')
                    break

                # If an error occurs tell the user to check
                except Exception as e:
                    print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
                    result = (0, 'Error', 1, str(e))

        # Else ask once and return zero value and error information
        else:
            answer_txt = input(question)

            # Let's try to convert input to numeric
            try:
                answer_txt = answer_txt.replace(',', '.')
                answer = float(answer_txt)
                result = (answer, 'OK', 0, 'Conversion successful')

            # If an error occurs tell the user to check
            except Exception as e:
                print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
                result = (0, 'Error', 1, str(e))

        return result

    # A static method to ask a question and convert the answer to a boolean without creating an object
    @staticmethod
    def ask_user_boolean(question, true_value, false_value, loop):
        """Asks a question and converts the answer to a boolean value

        Args:
            question (str): Question to ask
            true_value (str): value to use as True
            false_value (str): value to use as False
            loop (bool): If True asks the question until able to convert it

        Returns:
            tuple: answer as boolean, error message, error code, detailed error
        """

        # If loop argument is true use while loop until user inputs correct value
        prompt = f'{question}, vastaa {true_value}/{false_value}: '
        if loop == True:

            while True:
                answer_txt = input(prompt)
                answer_txt = answer_txt.lower()

                if answer_txt == true_value.lower():
                    answer = True
                    result = (answer, 'OK', 0, 'Conversion successful')
                    break
                elif answer_txt == false_value.lower():
                    answer = False
                    result = (answer, 'OK', 0, 'Conversion successful')
                    break
                else:
                    print('Virhe syötetyssä arvossa, sallitut arvot',
                          true_value, false_value)
                    result = ('N/A', 'Error', 1,
                              'unable to convert to boolean')

        # Else ask once and return zero value and error information
        else:
            answer_txt = input(prompt)
            answer_txt = answer_txt.lower()

            if answer_txt == true_value.lower():
                answer = True
                result = (answer, 'OK', 0, 'Conversion successful')
            elif answer_txt == false_value.lower():
                answer = False
                result = (answer, 'OK', 0, 'Conversion successful')
            else:
                print('Virhe syötetyssä arvossa, sallitut arvot',
                      true_value, false_value)
                result = ('N/A', 'Error', 1, 'unable to convert to boolean')

        return result

    #A method to ask a question and convert answer according to a dictionary
    @staticmethod
    def ask_user_dictionary(question, dictionary, loop):
        """Returns a value based on dictionary

        Args:
            question (str): The question to be asked
            dictionary (dict): Possible answers in key-value-pairs
            loop (bool): If True asks the question until able to convert it

        Returns:
            tuple: answer in correct type, error message, error code, detailed error
        """
        if loop == True:
            while True:
                answer_txt = input(question).lower()
                try:
                    value = dictionary[answer_txt]
                    result = (value, 'OK', 0, 'Conversion successful')
                    break
                except Exception as e:
                    result = ('N/A', 'Error', 1, str(e))
        
        else:
            answer_txt = input(question)
            try:
                value = dictionary[answer_txt]
                result = (value, 'OK', 0, 'Conversion successful')
            except Exception as e:
                 result = ('N/A', 'Error', 1, str(e))

        return result
    
if __name__ == "__main__":

    # Let's ask the weight and convert answer to a floating point number
    answer_and_error = Question.ask_user_float(
        'Kuinka paljon painat: ', True)
    print(answer_and_error)

    # Let's ask the age and convert it to an integer
    answer_and_error = Question.ask_user_integer('Kuinka vanha olet: ', True)
    print(answer_and_error)

    # Let's ask question and convert the answer to a boolean value
    answer_and_error = Question.ask_user_boolean('Oletko urheilullinen','Y', 'N', True)
    print(answer_and_error)

    gender_dictionary = {'tyttö': 0, 'poika': 1, 'mies': 1, 'nainen': 0}

    answer_and_error = Question.ask_user_dictionary('Sukupuoli: ', gender_dictionary, False)
    print(answer_and_error)

    