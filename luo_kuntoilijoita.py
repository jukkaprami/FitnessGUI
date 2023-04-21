# GET BASIC INFORMATION ABOUT AN ATHLETE AND CREATE ATHLETE OBJECTS
# -------------------------------------------------------

# LIBRARIES AND MODULES
import json
import kuntoilija
import questions


# Ask a question and convert the answer to float


# Enter information about an athlete
name = input('Nimi: ')
date_of_weighing = input('Punnituspaiva (vvvv-kk-pp): ')

# Ask details about her/him

weight = questions.Question.ask_user_float('Kuinka paljon painat (kg): ', True)[0]
height = questions.Question.ask_user_float('Kuinka pitkä olet (cm): ', True)[0]
age = questions.Question.ask_user_integer('Kuinka vanha olet ', True)[0]
allowed_genders = {'1' : 1, '0' : 0}
gender = questions.Question.ask_user_dictionary('Sukupuoli 1 mies, 0 nainen: ', allowed_genders, True)[0]
neck = questions.Question.ask_user_float('Mikä on kaulanympäryksesi (cm): ', True)[0]
waist = questions.Question.ask_user_float('Mikä on vyötärönympäryksesi: ', True)[0]

# If woman ask circumference of her hips
if gender == 0:
    hips = questions.Question.ask_user_float('Mikä on lantionympäryksesi: ', True)[0]

# Create an athelete object from Kuntoilija class
athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender, date_of_weighing)

# Print some information about the athlete
text_to_show = f'Terve {athlete.nimi}, painoindeksisi tänään on {athlete.bmi}'
print(text_to_show)
fat_percentage = athlete.rasvaprosentti()

# If male use usa_rasvaprosentti_mies method
if gender == 1:
    usa_fat_percentage = athlete.usa_rasvaprosentti_mies(height, waist, neck)
else:
    usa_fat_percentage = athlete.usa_rasvaprosentti_nainen(
        height, waist, hips, neck)

text_to_show = f'suomalainen rasva-% on {fat_percentage} ja amerikkalainen on {usa_fat_percentage}'
print(text_to_show)

print('nimi', athlete.nimi, 'paino', athlete.paino)

# athlete_data = [] # empty list for all athlete data

# Read previous athlete_data from disk

with open('athlete_data.json', 'r') as file:
    athlete_data = json.load(file)
    for item in athlete_data:
        print('paino oli' ,item['paino'])

# A dictionary for single weighing or an athlete
athlete_data_row = {'nimi': athlete.nimi, 'paino': athlete.paino, 'pituus': athlete.pituus, 'ika': athlete.ika, 'sukupuoli': athlete.sukupuoli, 'paiva': athlete.punnitus_paiva}

# Add a new data row to the athlete_data list
athlete_data.append(athlete_data_row)

# SAVE DATA TO A FILE

with open('athlete_data.json', 'w') as file:
    json.dump(athlete_data, file, indent=4)

