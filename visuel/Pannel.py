from pygame import *
from visuel.Game_Setup import *
from visuel.Heroes import *



init()


class text_base:                                                        #Define the texts
    def __init__(self, txt, x, y):
        self.text = font.Font.render(text_font_base, txt, True, Black)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (x, y)


    def draw(self):
        screen.blit(self.text, self.text_rect)



class display_hero_name:                                                #Define the heroes' name texts
    def __init__(self, name, x, y):
        self.text = font.Font.render(text_font_main, name, True, Black)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (x, y)


    def draw(self):
        screen.blit(self.text, self.text_rect)



class hp:                                                               #Define the heroes' hp texts
    def __init__(self, current_hp, max_hp, x, y):
        self.text0 = font.Font.render(text_font_base, current_hp, True, Black)
        self.text1 = font.Font.render(text_font_base, max_hp, True, Black)
        self.text_rect0 = self.text0.get_rect()
        self.text_rect1 = self.text1.get_rect()
        self.text_rect0.center = (x, y)
        self.text_rect1.center = (x+45, y)


    def draw(self):
        screen.blit(self.text0, self.text_rect0)
        screen.blit(self.text1, self.text_rect1)



class display_text:                                                     #Display the texts (Name of the Hero and hp)
    def __init__(self):
        for texte in text_bs:
            for heroe in display_name_text:
                for i in display_hp_text:
                    i.draw()
                    heroe.draw()       
                    texte.draw()



Heroes_text1 = text_base("HEROES", width/4, height-info_pannel+22)
Heroes_text2 = text_base("HEROES", 3*width/4, height-info_pannel+22)

text_bs = []
text_bs.append(Heroes_text1)
text_bs.append(Heroes_text2)
display_name_text = []
display_hp_text = []