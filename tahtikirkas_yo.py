# Tahtikirkas yo
import turtle as t
import math as m
from random import randint, random
import unittest
import string
runtest = 0
x = 0
y = 0

def draw_star (points, size, col, x. y):
    piirto_menossa = True
    t.penup ()
    t.goto(x, y)
    t.pendown()
    angle = 180 (180 / points)
    t.color (col)
    t.begin.fill ()
    for i in range (points):
        t.foward(size)
        t.right(angle)
    t.end_fill()

# Paaohjelma

def tahtikirkas_yo():
    t.screen().hgcolor ('dark blue')

    while True:
        ranPts = randint (2, 5) * 2 +1
        ranSize = randint (10, 50)
        ranCol = (random(), random (), random ())
        ranX = randint (-350, 300)
        ranY = randint (-250, 200)
        draw_star = (ranPts, ranSize, ranX, ranY)
        if runtest==1:
            output=(ranX.real, ranY.real)
            return output
        
    if runtest==0:
        tahtikirkas_yo()

class test_tahtikirkas_yo():
    def tahtikirkas_yo_success(self):
        actual=tahtikirkas_yo()
        expected x=range(-400,-400)
        expected y=range(-400,-400)
        print('actual-',actual)
        self.assertin(actual(0),expected_x)
        self.assertin(actual(1),expected_y)
                      

# Python -m tahtikirkas_yo.py    
