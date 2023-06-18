from pygame import *
from random import *



##Initilazing Pygame
init()


#initialise the variables
start = 1
running = False
mute_music = False
mouse_clicked = False
start_game = 0


clock = time.Clock()
fps = 60
info_pannel = 150
width = 1280
height = 720 + info_pannel

#coordinates for the panel texts
x1 = width/6
x2 = width/3
x3 = 2*width/3
x4 = 5*width/6
y1 = height-(info_pannel/2)

i1 = randint(0,3)   # for the background
i2 = randint(0,1)   # for the music

text_font_main = font.SysFont('Arial.ttf', 50)
text_font_base = font.SysFont('Arial.ttf', 40)
text_gold_left = font.SysFont('Arial.ttf', 80)

Black = (0,0,0)
White = (255,255,255)

screen = display.set_mode((width,height))
display.set_caption('Dragon Fantasy: Final Quest')