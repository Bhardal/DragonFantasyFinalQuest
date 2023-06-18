from pygame import *
from visuel.Game_Setup import *
from visuel.Villains import *
from visuel.Background import *



init()


##The different waves for each gamemode
def tuto_0():
    troll_A = villains(830, 250, 'Troll', 5, 2)                         #initiate values
    troll_B = villains(930, 370, 'Troll', 5, 2)
    troll_C = villains(1030, 490, 'Troll', 5, 2)

    troll_list_1 = []                                                   #Create the list of villains
    troll_list_1.append(troll_A)
    troll_list_1.append(troll_B)
    troll_list_1.append(troll_C)
    return(troll_list_1)


def tuto_1():
    troll_A = villains(730, 270, 'Troll', 5, 2)                         #initiate values
    troll_B = villains(830, 450, 'Troll', 5, 2)
    troll_C = villains(960, 270, 'Troll', 5, 2)
    troll_D = villains(1060, 450, 'Troll', 5, 2)

    troll_list_2 = []                                                   #Create the list of villains
    troll_list_2.append(troll_A)
    troll_list_2.append(troll_B)
    troll_list_2.append(troll_C)
    troll_list_2.append(troll_D)
    return(troll_list_2)


def tuto_2():
    troll_A = villains(860, 190, 'Troll', 5, 2)                         #initiate values
    troll_B = villains(960, 330, 'Troll', 5, 2)
    troll_C = villains(1060, 480, 'Troll', 5, 2)
    troll_D = villains(740, 290, 'Troll', 5, 2)
    troll_E = villains(840, 430, 'Troll', 5, 2)

    troll_list_3 = []                                                   #Create the list of villains
    troll_list_3.append(troll_A)
    troll_list_3.append(troll_B)
    troll_list_3.append(troll_C)
    troll_list_3.append(troll_D)
    troll_list_3.append(troll_E)
    return(troll_list_3)


def tuto_3():
    dragon = villains(750, 180, 'Dragon', 15, 2)                        #initiate values

    dragon_list = []                                                    #Create the list of villains
    dragon_list.append(dragon)
    return(dragon_list)


def story_0():
    goblin_A = villains(720, 360, 'goblin', 5, 2)                       #initiate values
    goblin_B = villains(820, 540, 'goblin', 5, 2)

    goblin_1_list = []                                                  #Create the list of villains
    goblin_1_list.append(goblin_A)
    goblin_1_list.append(goblin_B)
    return(goblin_1_list)


def story_1():
    goblin_A = villains(830, 350, 'goblin', 5, 2)                       #initiate values
    goblin_B = villains(930, 470, 'goblin', 5, 2)
    goblin_C = villains(1030, 590, 'goblin', 5, 2)

    goblin_2_list = []                                                  #Create the list of villains
    goblin_2_list.append(goblin_A)
    goblin_2_list.append(goblin_B)
    goblin_2_list.append(goblin_C)
    return(goblin_2_list)


def story_2():
    goblin_A = villains(860, 290, 'goblin', 5, 2)                       #initiate values
    goblin_B = villains(960, 430, 'goblin', 5, 2)
    goblin_C = villains(1060, 580, 'goblin', 5, 2)
    wolf_A = villains(720, 360, 'Wolf', 5, 2)
    wolf_B = villains(820, 540, 'Wolf', 5, 2)

    wolf_goblin_list = []                                               #Create the list of villains
    wolf_goblin_list.append(wolf_A)
    wolf_goblin_list.append(wolf_B)
    wolf_goblin_list.append(goblin_A)
    wolf_goblin_list.append(goblin_B)
    wolf_goblin_list.append(goblin_C)
    return(wolf_goblin_list)


def story_3():
    troll_A = villains(830, 250, 'Troll', 5, 2)                         #initiate values
    troll_B = villains(930, 370, 'Troll', 5, 2)
    troll_C = villains(1030, 490, 'Troll', 5, 2)

    troll_list = []                                                     #Create the list of villains
    troll_list.append(troll_A)
    troll_list.append(troll_B)
    troll_list.append(troll_C)
    return(troll_list)


def story_4():
    troll_A = villains(860, 190, 'Troll', 5, 2)                         #initiate values
    troll_B = villains(960, 330, 'Troll', 5, 2)
    troll_C = villains(1060, 480, 'Troll', 5, 2)
    wolf_A = villains(720, 360, 'Wolf', 5, 2)
    wolf_B = villains(820, 540, 'Wolf', 5, 2)

    wolf_troll_list = []                                                #Create the list of villains
    wolf_troll_list.append(wolf_A)
    wolf_troll_list.append(wolf_B)
    wolf_troll_list.append(troll_A)
    wolf_troll_list.append(troll_B)
    wolf_troll_list.append(troll_C)
    return(wolf_troll_list)
    

def story_5():
    dragon = villains(750, 180, 'Dragon', 15, 2)                        #initiate values

    dragon_list_1 = []                                                  #Create the list of villains
    dragon_list_1.append(dragon)
    return(dragon_list_1)


def story_6():
    demon_king = villains(850, 280, 'DemonKing', 15, 2)                 #initiate values

    demon_king_list = []                                                #Create the list of villains
    demon_king_list.append(demon_king)
    return(demon_king_list)


##Returning the correct ennemies for the current wave
def returnwave(gamemode, cw):
    if gamemode == "Tutorial":
        if cw == 0:
            return(tuto_0(), "Graveyard")
        elif cw == 1:
            return(tuto_1(), "Forest")
        elif cw == 2:
            return(tuto_2(), "Ruins")
        else:
            return(tuto_3(), "Castle")
    else:
        if cw == 0:
            return(story_0(), "Graveyard")
        elif cw == 1:
            return(story_1(), "Graveyard")
        elif cw == 2:
            return(story_2(), "Graveyard")
        elif cw == 3:
            return(story_3(), "Forest")
        elif cw == 4:
            return(story_4(), "Forest")
        elif cw == 5:
            return(story_5(), "Ruins")
        else:
            return(story_6(), "Castle")