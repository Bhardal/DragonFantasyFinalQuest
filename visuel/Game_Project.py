from json import load, dump
from random import randint
from time import sleep
from pygame import *
from visuel.Background import *
from visuel.Heroes import *
from visuel.Villains import *
from visuel.Pannel import *
from visuel.Current_Wave import *
from visuel.Text import *



##Initilazing Pygame
init()


##Opening items.json,  heroes.json and villains.json to get access to them
try:    
    with open('./project/data/items.json', 'r') as f:
        items = load(f)
except:
    try:
        with open('./data/items.json', 'r') as f:
            items = load(f)
    except:
        with open('../data/items.json', 'r') as f:
            items = load(f)

try:    
    with open('./project/data/heroes.json', 'r') as f:
        all_heroes = load(f)
except:
    try:
        with open('./data/heroes.json', 'r') as f:
            all_heroes = load(f)
    except:
        with open('../data/heroes.json', 'r') as f:
            all_heroes = load(f)

try:
    with open('./project/data/villains.json', 'r') as f:
        all_villains = load(f)
except:
    try:
        with open('./data/villains.json', 'r') as f:
            all_villains = load(f) 
    except:
        with open('../data/villains.json', 'r') as f:
            all_villains = load(f) 


##Waves by gamemode
Session3 = [["Troll"]]
Tutorial = [["Troll", "Troll", "Troll"], ["Troll", "Troll", "Troll", "Troll"], ["Troll", "Troll", "Troll", "Troll", "Troll"], ["Dragon"]]
Campaign = [["Goblin", "Goblin"], ["Goblin", "Goblin", "Goblin"], ["Wolf", "Wolf", "Goblin", "Goblin", "Goblin"], ["Troll2", "Troll2", "Troll2"], ["Wolf", "Wolf", "Troll2", "Troll2", "Troll2"], ["Dragon2"], ["Demon_King"]]
Werewolf = []                                                           #Won't be developped

GAMEMODES = {"Session3" : Session3, "Tutorial" : Tutorial, "Campaign" : Campaign, "Werewolfs" : Werewolf, "Nightmare" : Campaign} #available gamemodes


##Classes
class Game:
    def __init__(self, gamemode, cw):
        self.gamemode = gamemode
        if gamemode == "Session3" or gamemode == "Nightmare":           #Initializing the party size depending on the chosen gamemode
            self.party = {"t0" : "Warrior"}

        elif gamemode == "Tutorial" or gamemode == "Campaign":
            self.party = {"t0":"Warrior",
                    "t1":"Hunter",
                    "t2":"Sorcerer",
                    "t3":"Cleric"}
        self.wave = cw                                                  #Initializing the waves of ennemies according to the gamemode
        self.waves = GAMEMODES[self.gamemode]
        self.running = 1
        self.alive = 1
        #self.wave is the number of the one we're currently at, self.waves is the list of all the waves, and current_wave is when we play the wave


    ##Loading the save file
    def save(self):
        try:    
            with open('./project/data/save.json', 'r') as f:
                save = load(f)
        except:
            try:
                with open('./data/save.json', 'r') as f:
                    save = load(f)
            except:
                with open('../data/save.json', 'r') as f:
                    save = load(f)
        return(save)
    

    ##Saving progress into the file
    def saving(self, save):
        print("Saving...")
        try:    
            with open('./project/data/save.json', 'w') as f:
                dump(save, f, indent=4)
        except:
            try:
                with open('./data/save.json', 'w') as f:
                    dump(save, f, indent=4)
            except:
                with open('../data/save.json', 'w') as f:
                    dump(save, f, indent=4)


    def start(self):
        save = self.save()
        while self.wave <= len(self.waves)-1 and self.alive:
            gamemode = save['gm']
            current_wave1 = save['cw']
            villains_list, cb = returnwave(gamemode, current_wave1)     #Initialazing the scene for the fight
            current_wave = Fight(self.party, self.waves[self.wave], cb) #Initialazing the fight with the current wave of ennemies
            while self.running:
                self.running, self.alive = current_wave.turn(villains_list)#Each character attacks once             

            if self.alive:
                ##reupdating the heroes so that they appear alive at the start of the new wave
                hero_list_visual[0].action = 0
                hero_list_visual[0].frame_index = 0
                hero_list_visual[0].update()
                hero2.action = 0
                hero2.frame_index = 0
                hero2.update()
                hero3.action = 0
                hero3.frame_index = 0
                hero3.update()
                hero4.action = 0
                hero4.frame_index = 0
                hero4.update()
                display.flip()
                ##adding the gold for completing the wave
                if (save['cw'] == 3 and save['gm'] == "Tutorial") or  (save['cw'] == 5 and save['gm'] == "Campaign") or (save['cw'] == 5 and save['gm'] == "Nightmare"):
                    save['gold'] += 50
                if save['cw'] == 6:
                    save["gold"] += 100
                save['gold'] += 50
                self.saving(save)
                ##Going to the shop
                if not (save['cw'] == 6 and save["gm"] == "Nightmare"):
                    self.shop()
                save = self.save()
                ##Going to the next wave
                if self.alive:
                    self.wave += 1
                    save["lvl"] += 1
                    if self.wave != len(self.waves):
                        for _ in range(50):
                            print("\n")
                        print("NEXT WAVE !")
                        save['cw'] = self.wave
                        self.running = 1
                        next_wave().draw()
                        display.flip()
                        sleep(2)
                        self.saving(save)


        if self.alive:
            ##Changing gamemode/Finishing game
            if save["gm"] == "Tutorial":
                save["gm"] = "Campaign"
                save["cw"] = 0
                self.saving(save)
                return(1)
            elif save["gm"] == "Campaign":
                save["gm"] = "Nightmare"
                save["cw"] = 0
                hero_list_visual.clear()
                hero1 = heroes(135, 450, 'Warrior', 10)
                hero_list_visual.append(hero1)
                self.saving(save)
                return(1)
            else:
                game_over_win().draw()
                you_win()
                display.flip()
                for _ in range(50):
                    print("\n")    
                print("YOU WIN !")
                sleep(3)
                return(0)


    def shop(self):
        close = 1
        while close:
            ##ICI vraiment utile ?
            # clock.tick(fps)                                             #Set the framerate of the game
            save = self.save()
            shop_background().draw()
            item_bought = 0
            gold_left = str(save["gold"])
            draw_text(f"{gold_left} golds left", text_gold_left, Black, 20, height - info_pannel + 80)
            if item_1_button.draw():
                if "Wolf Claw Dagger" not in save["items"] and save["gold"] >= items["Wolf Claw Dagger"]["price"]:
                    print("You bought the Wolf Claw Dagger")
                    draw_text("You bought the Wolf Claw Dagger", text_font_main, Black, 20, height - info_pannel + 20)
                    save["items"].append("Wolf Claw Dagger")
                    save["gold"] -= items["Wolf Claw Dagger"]["price"]
                    self.saving(save)
                elif "Wolf Claw Dagger" in save["items"]:
                    print("You already possess this item")
                    draw_text("You already possess this item", text_font_main, Black, 20, height - info_pannel + 20)
                else:
                    print("You don't have enought gold")
                    draw_text("You don't have enough gold", text_font_main, Black, 20, height - info_pannel + 20)
                item_bought = 1
            if item_2_button.draw():
                if "Dragonbone Axe" not in save["items"] and save["gold"] >= items["Dragonbone Axe"]["price"]:
                    print("You bought the Dragonbone Axe")
                    draw_text("You bought the Dragonbone Axe", text_font_main, Black, 20, height - info_pannel + 20)
                    save["items"].append("Dragonbone Axe")
                    save["gold"] -= items["Dragonbone Axe"]["price"]
                    self.saving(save)
                elif "Dragonbone Axe" in save["items"]:
                    print("You already possess this item")
                    draw_text("You already possess this item", text_font_main, Black, 20, height - info_pannel + 20)
                else:
                    print("You don't have enought gold")
                    draw_text("You don't have enough gold", text_font_main, Black, 20, height - info_pannel + 20)
                item_bought = 1
            if item_3_button.draw():
                if "Hadar Orb" not in save["items"] and save["gold"] >= items["Hadar Orb"]["price"]:
                    print("You bought the Hadar Orb")
                    draw_text("You bought the Hadar Orb", text_font_main, Black, 20, height - info_pannel + 20)
                    save["items"].append("Hadar Orb")
                    save["gold"] -= items["Hadar Orb"]["price"]
                    self.saving(save)
                elif "Hadar Orb" in save["items"]:
                    print("You already possess this item")
                    draw_text("You already possess this item", text_font_main, Black, 20, height - info_pannel + 20)
                else:
                    print("You don't have enought gold")
                    draw_text("You don't have enough gold", text_font_main, Black, 20, height - info_pannel + 20)
                item_bought = 1
            if item_4_button.draw():
                if "Crusader's King Shield" not in save["items"] and save["gold"] >= items["Crusader's King Shield"]["price"]:
                    print("You bought the Crusader's King Shield")
                    draw_text("You bought the Crusader's King Shield", text_font_main, Black, 20, height - info_pannel + 20)
                    save["items"].append("Crusader's King Shield")
                    save["gold"] -= items["Crusader's King Shield"]["price"]
                    self.saving(save)
                elif "Crusader's King Shield" in save["items"]:
                    print("You already possess this item")
                    draw_text("You already possess this item", text_font_main, Black, 20, height - info_pannel + 20)
                else:
                    print("You don't have enought gold")
                    draw_text("You don't have enough gold", text_font_main, Black, 20, height - info_pannel + 20)
                item_bought = 1
            if item_5_button.draw():
                if "Darkhell stone" not in save["items"] and save["gold"] >= items["Darkhell stone"]["price"]:
                    print("You bought the Darkhell stone")
                    draw_text("You bought the Darkhell stone", text_font_main, Black, 20, height - info_pannel + 20)
                    save["items"].append("Darkhell stone")
                    save["gold"] -= items["Darkhell stone"]["price"]
                    self.saving(save)
                elif "Darkhell stone" in save["items"]:
                    print("You already possess this item")
                    draw_text("You already possess this item", text_font_main, Black, 20, height - info_pannel + 20)
                else:
                    print("You don't have enought gold")
                    draw_text("You don't have enough gold", text_font_main, Black, 20, height - info_pannel + 20)
                item_bought = 1
            if item_6_button.draw():
                if "Holy medicine bible" not in save["items"] and save["gold"] >= items["Holy medicine bible"]["price"]:
                    draw_text("You bought the Holy medicine bible", text_font_main, Black, 20, height - info_pannel + 20)
                    print("You bought the Holy medicine bible")
                    save["items"].append("Holy medicine bible")
                    save["gold"] -= items["Holy medicine bible"]["price"]
                    self.saving(save)
                elif "Holy medicine bible" in save["items"]:
                    print("You already possess this item")
                    draw_text("You already possess this item", text_font_main, Black, 20, height - info_pannel + 20)
                else:
                    print("You don't have enought gold")
                    draw_text("You don't have enough gold", text_font_main, Black, 20, height - info_pannel + 20)
                item_bought = 1
            if close_shop_button.draw():
                close = 0

            for events in event.get():                                  #Set the events
                if events.type == QUIT:                                 #Set the ways to quit the game (ESC or the cross)
                    quit()
                    self.alive = 0
                    close = 0
                elif events.type == KEYDOWN:
                    if events.key == K_ESCAPE:
                        quit()
                        self.alive = 0
                        close = 0

            if close:
                display.flip()
                if item_bought:
                    sleep(1.25)



class Fight:
    def __init__(self, party, ennemies, cb):
        self.hero = Character(party["t0"], "heroes", "None", x1, y1)
        self.t1 = NoCharacter()
        self.t2 = NoCharacter()
        self.t3 = NoCharacter()
        self.hps = len(party)                                           #Heroes Party Size
        self.cb = cb
        if self.hps >= 2:
            self.t1 = Character(party["t1"], "heroes", "None", x2, y1)
            self.t2 = Character(party["t2"], "heroes", "None", x3, y1)
            self.t3 = Character(party["t3"], "heroes", "None", x4, y1)

        self.eps = len(ennemies)                                        #Ennemy Party Size
        if len(ennemies) >= 1:
            self.v1 = Character(ennemies[0], "villains", str(all_villains[ennemies[0]][1])+" A")
            self.v2 = NoCharacter()
            self.v3 = NoCharacter()
            self.v4 = NoCharacter()
            self.v5 = NoCharacter()
            self.v6 = NoCharacter()

        if len(ennemies) >= 2:
            self.v2 = Character(ennemies[1],"villains", str(all_villains[ennemies[1]][1])+" B")

        if len(ennemies) >= 3:
            self.v3 = Character(ennemies[2],"villains", str(all_villains[ennemies[2]][1])+" C")

        if len(ennemies) >= 4:
            self.v4 = Character(ennemies[3],"villains", str(all_villains[ennemies[3]][1])+" D")

        if len(ennemies) >= 5:
            self.v5 = Character(ennemies[4],"villains", str(all_villains[ennemies[4]][1])+" E")

        self.villains = [self.v1, self.v2, self.v3, self.v4, self.v5, self.v6]
    

    ##Loading the save file
    def save(self):
        try:    
            with open('./project/data/save.json', 'r') as f:
                save = load(f)
        except:
            try:
                with open('./data/save.json', 'r') as f:
                    save = load(f)
            except:
                with open('../data/save.json', 'r') as f:
                    save = load(f)
        return(save)


    def turn(self, villains_list):                                      #One round. all heroes attack once if alive.
        if (self.hero.hp > 0 or self.t1.hp > 0 or self.t2.hp > 0 or self.t3.hp > 0) and (self.v1.hp > 0 or self.v2.hp > 0 or self.v3.hp > 0 or self.v4.hp > 0 or self.v5.hp > 0):
            saveAndQuit = 1
            save = self.save()
            if self.attack(self.hero, villains_list):
                if save["gm"] != "Nightmare":
                    if self.attack(self.t1, villains_list):
                        if self.attack(self.t2, villains_list):
                            if self.attack(self.t3, villains_list):
                                saveAndQuit = 0
                else:
                    saveAndQuit = 0

            
            if saveAndQuit:                                             #If the game is closed during execution
                save = self.save()
                ##Saving progress into the file
                print("Saving...")
                try:    
                    with open('./project/data/save.json', 'w') as f:
                        dump(save, f, indent=4)
                except:
                    try:
                        with open('./data/save.json', 'w') as f:
                            dump(save, f, indent=4)
                    except:
                        try:
                            with open('../data/save.json', 'w') as f:
                                dump(save, f, indent=4)
                        except:
                            print("failed to save")
                print("Exiting")
                return(0, 0)

        ##Checking if the party didn't survive the fight
        if not(self.hero.hp > 0 or self.t1.hp > 0 or self.t2.hp > 0 or self.t3.hp > 0):
            for _ in range(10):
                print("\n")
            print(f"{self.hero.name}'s party died honorably in battle, for its country and its people. \
Imanity will forever remember their bravery")
            for _ in range(50):
                print("\n")
            print("Game Over")
            game_over_lose().draw()
            display.flip()
            sleep(3)
            return(0, 0)
        
        ##Checking if there are still ennemies standing
        elif (self.v1.hp > 0 or self.v2.hp > 0 or self.v3.hp > 0 or self.v4.hp > 0 or self.v5.hp > 0):
            return(1, 1)
        
        else:
            return(0, 1)
    

    def attack(self, h, villains_list, ennemy=None):
        save = self.save()
        display_hp_text.clear()
        display_hp_text.append(hp(f"{self.hero.hp}", f"/ {self.hero.maxhp}", self.hero.x-25, self.hero.y+45))
        if self.hps > 1:
            display_hp_text.append(hp(f"{self.t1.hp}", f"/ {self.t1.maxhp}", self.t1.x-25, self.t1.y+45))
            display_hp_text.append(hp(f"{self.t2.hp}", f"/ {self.t2.maxhp}", self.t2.x-25, self.t2.y+45))
            display_hp_text.append(hp(f"{self.t3.hp}", f"/ {self.t3.maxhp}", self.t3.x-25, self.t3.y+45))
        bg = background()
        bg.draw(self.cb)
        display_text()
        for hero_ in hero_list_visual:                                  #Display the heroes
            hero_.draw()
        for dfhjkl in villains_list:
            dfhjkl.draw()
        display.flip()
        if h.hp > 0:
            ##Initialzing / updating the scene for the first time of the turn
            bg = background()
            bg.draw(self.cb)                                            #Display the Background
            display_text()
            display_heroes()
            
            for eachEnnemy in villains_list:
                eachEnnemy.update()
                eachEnnemy.draw()

            for events in event.get():                                  #Set the events
                if events.type == QUIT:                                 #Set the ways to quit the game (ESC or the cross)
                    quit()
                    return(0)
                elif events.type == KEYDOWN:
                    if events.key == K_ESCAPE:
                        quit()
                        return(0)

            display.flip()

            ##Checking if an ennemy is alive
            if (self.v1.hp > 0 or self.v2.hp > 0 or self.v3.hp > 0 or self.v4.hp > 0 or self.v5.hp > 0):
                ennemy = 5
                while self.villains[ennemy].hp <= 0:                    #Randomly choosing an ennemy to attack
                    ##Initialzing / updating the scene for the second time of the turn
                    bg = background()
                    bg.draw(self.cb)                                    #Display the Background
                    display_text()
                    display_heroes()
                    
                    for eachEnnemy in villains_list:
                        eachEnnemy.update()
                        eachEnnemy.draw()

                    for events in event.get():                          #Set the events
                        if events.type == QUIT:                         #Set the ways to quit the game (ESC or the cross)
                            quit()
                            return(0)
                        elif events.type == KEYDOWN:
                            if events.key == K_ESCAPE:
                                quit()
                                return(0)
                            
                        if events.type == MOUSEBUTTONDOWN:
                            pos = mouse.get_pos()                       #Take the position of the mouse cursor
                            for count, vil in enumerate(villains_list):
                                if vil.rect.collidepoint(pos):          #Look if the mouse cursor go over the ennemy position
                                    ennemy = count                      #Establish the ennemy variable to the clicked ennemy
                    display.flip()

                ##Starting the dealing damage stuff
                dmg = randint(h.minatk, h.atk)
                if "Dragonbone Axe" in save["items"]:
                    dmg += 2
                dmg2 = 0
                if h.creature == "Hunter":                              #Specificities of the Hunter
                    ##Checking the number of arrow left, and dealing damage accordingly
                    if h.quiver == 0:
                        dmg = randint(0, 1)
                        if "Wolf Claw Dagger" in save["items"]:
                            dmg += 1
                    else:
                        h.quiver -= 1

                if h.creature == "Sorcerer":                            #Specificities of the Sorcerer (Mage)
                    ##Creating the splash damage
                    dmg2 = randint(0+save["lvl"]//5,2+save["lvl"]//5)
                    if "Hadar Orb" in save["items"]:
                        dmg2 += 1
                        dmg += 1
                    self.v1.hp -= dmg2
                    self.v2.hp -= dmg2
                    self.v3.hp -= dmg2
                    self.v4.hp -= dmg2
                    self.v5.hp -= dmg2
                
                if h.creature == "Cleric":                              #Specificities of the Cleric (Priest)
                    ##Seeking the most injured hero to heal
                    min = h.hp
                    if 0 < self.hero.hp <= min:
                        min = self.hero.hp
                        who = 'hero'
                    if 0 < self.t1.hp <= min:
                        min = self.t1.hp
                        who = 't1'
                    if 0 < self.t2.hp <= min:
                        min = self.t2.hp
                        who = 't2'
                    if 0 < self.t3.hp <= min:
                        min = self.t3.hp
                        who = 't3'
                    #Healing the most injured hero
                    heal = 2
                    if "Holy medicine bible" in save["items"]:
                        heal = 3
                    if who == 'hero':
                        self.hero.hp += heal
                    elif who == 't1':
                        self.t1.hp += heal
                    elif who == 't2':
                        self.t2.hp += heal
                    elif who == 't3':
                        self.t3.hp += heal
                self.villains[ennemy].hp -= dmg-dmg2                    #dealing damages

                ##Attack animations
                if h.name == self.hero.name:
                    hero_list_visual[0].heroes_atk()
                elif h.name == self.t1.name:
                    hero2.heroes_atk()
                elif h.name == self.t2.name:
                    hero3.heroes_atk()
                else:
                    hero4.heroes_atk()
                
                ##Initialzing / updating the scene for the third time of the turn
                for _ in range(9):
                    bg = background()
                    bg.draw(self.cb)                                        #Display the Background
                    display_text()
                    display_heroes()
                    for eachEnnemy in villains_list:
                        eachEnnemy.update()
                        eachEnnemy.draw()

                    for events in event.get():                              #Set the events
                        if events.type == QUIT:                             #Set the ways to quit the game (ESC or the cross)
                            quit()
                            return(0)
                        elif events.type == KEYDOWN:
                            if events.key == K_ESCAPE:
                                quit()
                                return(0)
                    draw_text_background(0,0)
                    draw_text(f"{h.name} attacks {self.villains[ennemy].name} and deals {dmg} damages to him !", text_font_main, White, width/6, 15)
                    display.flip()

                print(f"{h.name} attacks {self.villains[ennemy].name} and deals {dmg} damages to him !")
 
                for v in range(self.eps):                               #Rounding up the ennemy's hp to 0 if dead
                    # print(self.villains[v].name, self.villains[v].hp)
                    if self.villains[v].hp <= 0:
                        if self.villains[v].name != "None":
                            print(self.villains[v].name, self.villains[v].hp)
                            print(f"{self.villains[v].name} is DED")
                        self.villains[v] = NoCharacter(None, "villains", None, None, v, villains_list)


                ##Initialzing / updating the scene for the fourth time of the turn
                bg = background()
                bg.draw(self.cb)                                        #Display the Background
                display_text()
                display_heroes()
                for eachEnnemy in villains_list:
                    eachEnnemy.update()
                    eachEnnemy.draw()

                for events in event.get():                              #Set the events
                    if events.type == QUIT:                             #Set the ways to quit the game (ESC or the cross)
                        quit()
                        return(0)
                    elif events.type == KEYDOWN:
                        if events.key == K_ESCAPE:
                            quit()
                            return(0)
                display.flip()

                if self.villains[ennemy].hp > 0:                        #Ennemy's turn to deal damage, if alive
                    dmg = randint(0, self.villains[ennemy].atk)
                    dmg2 = 0
                    if self.villains[ennemy].creature == "Dragon" or self.villains[ennemy].creature == "Dragon2":#Specificities of the Dragon
                        #Creating the splash damage
                        dmg2 = randint(0+save["lvl"]//5,2+(save["lvl"]+2)//5)
                        self.hero.hp -= dmg2
                        self.t1.hp -= dmg2
                        self.t2.hp -= dmg2
                        self.t3.hp -= dmg2
                    #Dealing damages
                    h.hp -= dmg-dmg2
                    print(f"{self.villains[ennemy].name} attacks {h.name} and deals {dmg} damages to him !")
                    if self.hero.hp <= 0:
                        print(f"{self.hero.name} is DED")
                        self.hero = NoCharacter(self.hero.creature, "heroes", self.hero.x, self.hero.y, 0)
                    if self.hps > 1:
                        if self.t1.hp <= 0:
                            print(f"{self.t1.name} is DED")
                            self.t1 = NoCharacter(self.t1.creature, "heroes", self.t1.x, self.t1.y, 1)
                        if self.t2.hp <= 0:
                            print(f"{self.t2.name} is DED")
                            self.t2 = NoCharacter(self.t2.creature, "heroes", self.t2.x, self.t2.y, 2)
                        if self.t3.hp <= 0:
                            print(f"{self.t3.name} is DED")
                            self.t3 = NoCharacter(self.t3.creature, "heroes", self.t3.x, self.t3.y, 3)
                    print(f"{h.name} has {h.hp}hp left")


        display_hp_text.clear()
        display_hp_text.append(hp(f"{self.hero.hp}", f"/ {self.hero.maxhp}", self.hero.x-25, self.hero.y+45))
        if self.hps > 1:
            display_hp_text.append(hp(f"{self.t1.hp}", f"/ {self.t1.maxhp}", self.t1.x-25, self.t1.y+45))
            display_hp_text.append(hp(f"{self.t2.hp}", f"/ {self.t2.maxhp}", self.t2.x-25, self.t2.y+45))
            display_hp_text.append(hp(f"{self.t3.hp}", f"/ {self.t3.maxhp}", self.t3.x-25, self.t3.y+45))
        bg = background()
        bg.draw(self.cb)
        display_text()
        for hero_ in hero_list_visual:                                         # Display the heroes
            hero_.draw()
        for dfhjkl in villains_list:
            dfhjkl.draw()
        display.flip()
        return(1)



class Character:
    def __init__(self, creature, group="heroes", name = "None", x_coord=None, y_coord=None):
        if group == "heroes":
            ##Loading the save file
            try:    
                with open('./project/data/save.json', 'r') as f:
                    save = load(f)
            except:
                try:
                    with open('./data/save.json', 'r') as f:
                        save = load(f)
                except:
                    with open('../data/save.json', 'r') as f:
                        save = load(f)
            self.hp = all_heroes[creature][0]
            self.maxhp = all_heroes[creature][0]
            if "Crusader's King Shield" in save["items"]:
                self.hp += 5
                self.maxhp += 5
            if "Darkhell stone" in save["items"]:
                self.hp += 10
                self.maxhp += 10
            self.name = all_heroes[creature][1]
            self.minatk = save["lvl"]//2
            if save["lvl"] != 10:
                self.atk = all_heroes[creature][2] + ((save["lvl"]-1)//2)
            else:
                self.atk = all_heroes[creature][2] + 5
            self.creature = creature
            self.x = x_coord
            self.y = y_coord
            if save["gm"] == "Nightmare":
                display_name_text.clear()
            display_name = display_hero_name(self.name, self.x, self.y)
            display_name_text.append(display_name)
            display_hp = hp(f"{self.hp}", f"/ {self.maxhp}", self.x-25, self.y+45)
            display_hp_text.append(display_hp)
            display.flip()
            if self.creature == "Hunter":
                self.quiver = 5

        elif group == "villains":
            self.hp = all_villains[creature][0]
            self.name = name
            self.atk = all_villains[creature][2]
            self.creature = creature



class NoCharacter:
    def __init__(self, creature=None, group="None", x_coord=None, y_coord=None, numero=None, vl=None):
        self.hp = 0
        self.name = "None"
        self.atk = 0
        if group == "heroes":
            ##Loading the save file
            try:    
                with open('./project/data/save.json', 'r') as f:
                    save = load(f)
            except:
                try:
                    with open('./data/save.json', 'r') as f:
                        save = load(f)
                except:
                    with open('../data/save.json', 'r') as f:
                        save = load(f)
            self.maxhp = all_heroes[creature][0]
            if "Crusader's King Shield" in save["items"]:
                self.maxhp += 5
            if "Darkhell stone" in save["items"]:
                self.maxhp += 10
            self.name = all_heroes[creature][1]
            self.creature = creature
            self.x = x_coord
            self.y = y_coord
            if numero == 0:
                hero1.heroes_dead()
                hero1.alive_visual = False
            elif numero == 1:
                hero2.heroes_dead()
                hero2.alive_visual = False
            elif numero == 2:
                hero3.heroes_dead()
                hero3.alive_visual = False
            else:
                hero4.heroes_dead()
                hero4.alive_visual = False
            display_heroes()
        elif group == "villains":
            vl[numero].notded = 0