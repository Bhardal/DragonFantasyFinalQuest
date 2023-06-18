from pygame import *
from visuel.Game_Setup import *



init()


class villains():
    def __init__(self, x, y, name, max_hp, atk):
        self.name = name                                                #establish the name of the villains (for the location of the directory)
        self.max_hp = max_hp                                            #establish the maximun HP of the villains
        self.hp = max_hp                                                #establish the current HP of the villains (initialize at max HP)
        self.atk = atk                                                  #establish the attack of the villains
        self.alive = True                                               #establish that the villains are alive
        self.animation_idle =[]
        self.frame_index = 0
        self.notded = 1                                                 #if villains is alive or not
        self.update_time = time.get_ticks()
        for i in range(4):
            try:
                img = image.load(f"./img/Villains/{self.name}/Idle/{i}.png").convert_alpha()
            except:
                try:
                    img = image.load(f"./visuel/img/Villains/{self.name}/Idle/{i}.png").convert_alpha()
                except:
                    img = image.load(f"./grrafik/visuel/img/Villains/{self.name}/Idle/{i}.png").convert_alpha()
            self.animation_idle.append(img)
        self.image = self.animation_idle[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


    def update(self):
        if self.notded:
            animation_cooldown = 200
            self.image = self.animation_idle[self.frame_index]
            ##check if enough time has passed since the last update
            if time.get_ticks() - self.update_time > animation_cooldown:
                self.update_time = time.get_ticks()
                self.frame_index += 1
            ##reset animation back to start
            if self.frame_index >= len(self.animation_idle):
                self.frame_index = 0


    def draw(self):
        if self.notded:
            screen.blit(self.image, self.rect)