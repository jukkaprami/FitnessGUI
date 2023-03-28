# Yhdeksan Henkeä
import random
import unittest
lives = 9
words = ['pizza', 'keiju', 'kieli', 'paita', 'sorsa', 'kirje']
secret_word = random.choice (words)
print(secret_word)
clue = list('????')
heart_symbol = u'\u2764'
guessed_word_correctly = False

def update_clue (guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
            index = index +1

while lives > 0:
    print(clue)
    print('henkia jaljella: ' + heart_symbol * lives)
    guess = input (' Arvaa kirjain tai koko sana:')
    if guess in secret_word:
        update_clue (guess, secret_word, clue)
    else:
        print('vaarin. menetit yhden hengen.')
        lives = lives -1
        if lives == 0:
            print ('havisit!, Salainen sana oli ', + secret_word)
    if guess == secret_word:
        guessed_word_correctly = True
        #print(guessed_word_correctly)
        if guessed_word_correctly:
            print ('voitit!, salainen sana oli ' + secret_word)
            break