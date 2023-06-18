from pygame import *
from visuel.Heroes import *
from visuel.Villains import *
from visuel.Background import *
from visuel.Current_Wave import *
from visuel.Pannel import *
from visuel.Text import *
from visuel.Game_Project import *
from visuel.Button import *



init()              


def opensave():
    try:    
        with open('./project/data/save.json', 'r') as f:
            save = load(f)
    except:
        try:
            with open('./data/save.json', 'r') as f:
                save = load(f)
        except:
            with open('./save.json', 'r') as f:
                save = load(f)
    return(save)


start_bg = start_background()
while start:                                                            #While loop to display the game
    clock.tick(fps)                                                     #Set the framerate of the game
    start_bg.draw()
    if mute_music_button_on.draw():                                     #Mute button (press once to mute, and again to unmute)
            if mute_music == False:
                mixer_music.set_volume(0)
                mute_music = True
            else:
                mixer_music.set_volume(0.2)
                mute_music = False

    if restart_button.draw():                                           #Set a button to reset the save
        save = {"gm": "Tutorial", "lvl": 1, "cw": 0, "gold": 0, "items": []}
        try:    
            with open('./project/save.json', 'w') as f:
                dump(save, f, indent=4)
        except:
            try:
                with open('./project/data/save.json', 'w') as f:
                    dump(save, f, indent=4)
            except:
                try:
                    with open('./data/save.json', 'w') as f:
                        dump(save, f, indent=4)
                except:
                    with open('./save.json', 'w') as f:
                        dump(save, f, indent=4)

    for events in event.get():                                          #Set the events
        if events.type == QUIT:                                         #Set the ways to quit the game (ESC or the cross)
            start = False
            running = False
        elif events.type == KEYDOWN:
            if events.key == K_ESCAPE:
                start = False
                running = False        
            if events.key == K_RETURN:
                save = opensave()
                launchGame = Game(save['gm'], save['cw']) 
                if save["gm"] == "Nightmare":
                    hero_list_visual.clear()
                    hero1 = heroes(135, 450, 'Warrior', 10)
                    hero_list_visual.append(hero1)   
                if launchGame.start():
                    save = opensave()
                    launchGame2 = Game(save['gm'], save['cw'])
                    if save["gm"] == "Nightmare":
                        hero_list_visual.clear()
                        hero1 = heroes(135, 450, 'Warrior', 10)
                        hero_list_visual.append(hero1)
                    gamemode_completed().draw(1)
                    display.flip()
                    sleep(3)
                    if launchGame2.start():
                        save = opensave()
                        launchGame3 = Game(save["gm"], save["cw"])
                        hero_list_visual.clear()
                        hero1 = heroes(135, 450, 'Warrior', 10)
                        hero_list_visual.append(hero1)
                        gamemode_completed().draw(2)
                        display.flip()
                        sleep(3)
                        launchGame3.start()
                start = 0

    if start:
        display.flip()      
quit()