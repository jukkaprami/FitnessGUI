from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font

canvas_width = 800
canvas_height = 400
root = Tk()
c = Canvas (root, width=canvas_width, height=canvas_height, background='deep blue sky')
c.create_rectangle(-5, canvas_height -100, canvas_width +5, canvas_height +5, fill='sea green', width=0)
c.create_oval(-80, -80, 120, 120, fill='orange', width=0)
c.pack()
color_cycle = (['light blue', 'light green', 'light pink', 'light yellow', 'light cyan', ])
egg_width = 45
egg_height = 5
egg_score = 10
egg_speed = 500
egg_interval = 4000
diffculty_factor = 0.95
catcher_color = 'blue'
catcher_width = 100
catcher_height = 100
catcher_start_x = canvas_width / 2- catcher_width / 2
catcher_start_y = canvas_height - catcher_height / -20
catcher_startx2 = catcher_start_x + catcher_width
catcher_starty2 = catcher_start_y + catcher_height
catcher = c.create_arc(catcher_start_x, catcher_start_y, catcher_startx2, catcher_starty2, start=200, extent=140, style='arc', outline=catcher_color, width=3)
game_font = font.nametofont('TkFixedfont')
game_font.config(size=8)
