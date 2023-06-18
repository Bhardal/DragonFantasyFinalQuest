from pygame import *
from visuel.Game_Setup import *



init()


class heroes():
    def __init__(self, x, y, name, max_hp):
        self.name = name                                                #establish the name of the character (for the location of the directory)
        self.max_hp = max_hp                                            #establish the maximun HP of the characters
        self.hp = max_hp                                                #establish the current HP of the characters (initialize at max HP)
        self.alive_visual = True                                        #establish that the characters are Alive
        self.animation_list =[]
        self.frame_index = 0
        self.action = 0                                                 #0 : Idle / 1 : Attack / 2 : Dead
        self.update_time = time.get_ticks()
        temp_list = []                                                  #set a temporary list of IDLE
        for i in range(4):                                              
            try:                                                        
                img = image.load(f"./img/Heroes/{self.name}/Idle/{i}.png").convert_alpha()
            except:
                try:
                    img = image.load(f"./visuel/img/Heroes/{self.name}/Idle/{i}.png").convert_alpha()
                except:
                    img = image.load(f"./Project/visuel/img/Heroes/{self.name}/Idle/{i}.png").convert_alpha()
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []                                                  #set a temporary list of Attack
        for i in range(4):
            try:
                img = image.load(f"./img/Heroes/{self.name}/ATK/{i}.png").convert_alpha()
            except:
                try:
                    img = image.load(f"./visuel/img/Heroes//{self.name}/ATK/{i}.png").convert_alpha()
                except:
                    img = image.load(f"./Project/visuel/img/Heroes/{self.name}/ATK/{i}.png").convert_alpha()
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []                                                  #set a temporary list of Attack
        for i in range(4):
            try:
                img = image.load(f"./img/Heroes/{self.name}/Dead/{i}.png").convert_alpha()
            except:
                try:
                    img = image.load(f"./visuel/img/Heroes//{self.name}/Dead/{i}.png").convert_alpha()
                except:
                    img = image.load(f"./Project/visuel/img/Heroes/{self.name}/Dead/{i}.png").convert_alpha()
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


    def update(self):
        animation_cooldown = 200
        self.image = self.animation_list[self.action][self.frame_index]
        ##check if enough time has passed since the last update
        if time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = time.get_ticks()
            self.frame_index += 1
        ##reset animation back to start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.idle()


    def idle(self):
        self.frame_index = 0
        self.update_time = time.get_ticks()
        if self.alive_visual:
            self.action = 0


    def heroes_atk(self):
        self.action = 1
        self.frame_index = 0
        self.update_time = time.get_ticks()


    def heroes_dead(self):
        self.action = 2
        self.frame_index = 0
        self.update_time = time.get_ticks()
 

    def draw(self):
        screen.blit(self.image, self.rect)



class display_heroes:
    def __init__(self):
        for hero_ in hero_list_visual:                                         # Display the heroes
            hero_.update()
            hero_.draw()



hero1 = heroes(210, 360, 'Warrior', 10)
hero2 = heroes(160, 420, 'Ranger', 10)
hero3 = heroes(110, 480, 'Sorcerer', 10)
hero4 = heroes(60, 540, 'Cleric', 10)

hero_list_visual = []
hero_list_visual.append(hero1)
hero_list_visual.append(hero2)
hero_list_visual.append(hero3)
hero_list_visual.append(hero4)