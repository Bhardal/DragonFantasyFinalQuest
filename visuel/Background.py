from pygame import *
from visuel.Game_Setup import *
from visuel.Button import *



init()


##To draw the background during the waves
class background():
    def __init__(self):
        pass


    def draw(self, b):
        try:
            bg_castle = image.load("./img/Background/0.png").convert_alpha()
            bg_ruins = image.load("./img/Background/1.png").convert_alpha()
            bg_forest = image.load("./img/Background/2.png").convert_alpha()
            bg_graveyard = image.load("./img/Background/3.png").convert_alpha()
        except:
            try:
                bg_castle = image.load("./visuel/img/Background/0.png").convert_alpha()
                bg_ruins = image.load("./visuel/img/Background/1.png").convert_alpha()
                bg_forest = image.load("./visuel/img/Background/2.png").convert_alpha()
                bg_graveyard = image.load("./visuel/img/Background/3.png").convert_alpha()
            except:
                bg_castle = image.load("./Project/visuel/img/Background/0.png").convert_alpha()
                bg_ruins = image.load("./Project/visuel/img/Background/1.png").convert_alpha()
                bg_forest = image.load("./Project/visuel/img/Background/2.png").convert_alpha()
                bg_graveyard = image.load("./Project/visuel/img/Background/3.png").convert_alpha()
        
        try:
            img_panel = image.load("./img/Panel/5.png").convert_alpha()
        except:
            try:
                img_panel = image.load("./visuel/img/Panel/5.png").convert_alpha()
            except:
                img_panel = image.load("./Project/visuel/img/Panel/5.png").convert_alpha()
        
        if b == "Castle":
            screen.blit(bg_castle, (0,0))
        elif b == "Ruins":
            screen.blit(bg_ruins, (0,0))
        elif b == "Forest":
            screen.blit(bg_forest, (0,0))
        else:
            screen.blit(bg_graveyard, (0,0))
        screen.blit(img_panel, (0,height-info_pannel))



##The background when the game is started
class start_background:
    def __init__(self):
        pass


    def draw(self):
        try:
            bg = image.load("./img/Start_Background/0.png").convert_alpha()
        except:
            try:
                bg = image.load("./visuel/img/Start_Background/0.png").convert_alpha()
            except:
                bg = image.load("./Project/visuel/img/Start_Background/0.png").convert_alpha()
    
        screen.blit(bg, (0,0))



##The "Next wave - All the characters have been healed" panel
class next_wave():
    def __init__(self):
        pass


    def draw(self):
        try:
            bg = image.load("./img/Next_Wave/0.png").convert_alpha()
        except:
            try:
                bg = image.load("./visuel/img/Next_Wave/0.png").convert_alpha()
            except:
                bg = image.load("./Project/visuel/img/Next_Wave/0.png").convert_alpha()
      
        screen.blit(bg, (0,0))



##The background when going from a gamemode to the other
class gamemode_completed():
    def __init__(self):
        pass


    def draw(self, gm):
        try:
            tuto_complete_img = image.load("./img/GamemodeComplete/0.png").convert_alpha()
            campaign_complete_img = image.load("./img/GamemodeComplete/1.png").convert_alpha()
        except:
            try:
                tuto_complete_img = image.load("./visuel/img/GamemodeComplete/0.png").convert_alpha()
                campaign_complete_img = image.load("./visuel/img/GamemodeComplete/1.png").convert_alpha()
            except:
                tuto_complete_img = image.load("./Project/visuel/img/GamemodeComplete/0.png").convert_alpha()
                campaign_complete_img = image.load("./Project/visuel/img/GamemodeComplete/1.png").convert_alpha()
        if gm == 1:
            screen.blit(tuto_complete_img, (0,0))
        elif gm == 2:
            screen.blit(campaign_complete_img, (0,0))



##The reset save button
class continue_or_restart():
    def __init__(self):
        pass


    def draw(self):
        try:
            continue_or_restart_img = image.load("./img/ResetBackground/0.png").convert_alpha()
        except:
            try:
                continue_or_restart_img = image.load("./visuel/img/ResetBackground/0.png").convert_alpha()
            except:
                continue_or_restart_img = image.load("./Project/visuel/img/ResetBackground/0.png").convert_alpha()
                
        screen.blit(continue_or_restart_img, (0,0))



##The win ending background
class game_over_win():
    def __init__(self):
        pass


    def draw(self):
        try:
            win_img = image.load("./img/GameOver/0.png").convert_alpha()
        except:
            try:
                win_img = image.load("./visuel/img/GameOver/0.png").convert_alpha()
            except:
                win_img = image.load("./Project/visuel/img/GameOver/0.png").convert_alpha()
       
        screen.blit(win_img, (0,0))



##The game over ending background
class game_over_lose():
    def __init__(self):
        pass


    def draw(self):
        try:
            lose_img = image.load("./img/GameOver/1.png").convert_alpha()
        except:
            try:
                lose_img = image.load("./visuel/img/GameOver/1.png").convert_alpha()
            except:
                lose_img = image.load("./Project/visuel/img/GameOver/1.png").convert_alpha()
                
        screen.blit(lose_img, (0,0))



##The shop background
class shop_background():
    def __init__(self):
        pass


    def draw(self):
        try:
            shop_img = image.load("./img/Shop/7.png").convert_alpha()
        except:
            try:
                shop_img = image.load("./visuel/img/Shop/7.png").convert_alpha()
            except:
                shop_img = image.load("./Project/visuel/img/Shop/7.png").convert_alpha()

        screen.blit(shop_img, (0,0))