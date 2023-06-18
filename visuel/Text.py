from pygame import *
from visuel.Game_Setup import *



init()


try:
    img_txt_bg = image.load("./img/Txt/0.png").convert_alpha()
except:
    try:
        img_txt_bg = image.load("./visuel/img/Txt/0.png").convert_alpha()
    except:
        img_txt_bg = image.load("./Project/visuel/img/Txt/0.png").convert_alpha()


def draw_text_background(x, y):
    rect = img_txt_bg.get_rect()    
    rect.topleft = (x, y)
    screen.blit(img_txt_bg, rect.topleft)


def draw_text(text, font, text_col, x, y):
	img_txt = font.render(text, True, text_col)
	screen.blit(img_txt, (x, y))