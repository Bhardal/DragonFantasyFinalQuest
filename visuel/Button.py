from pygame import *
from visuel.Game_Setup import *



init()


##How to create a clickable button
class Button():
	def __init__(self, surface, x, y, image, size_x, size_y):
		self.image = transform.scale(image, (size_x, size_y))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
		self.surface = surface


	def draw(self):
		action = False
		#get mouse position
		pos = mouse.get_pos()
		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button
		self.surface.blit(self.image, (self.rect.x, self.rect.y))
		return(action)



#for the music
try:
    mute_sound_img = image.load("./img/Mute/0.png").convert_alpha()
    mixer_music.load(f"./Audio/{i2}.ogg")
except:
    try:
        mute_sound_img = image.load("./visuel/img/Mute/0.png").convert_alpha()
        mixer_music.load(f"./visuel/Audio/{i2}.ogg")
    except:
        mute_sound_img = image.load("./Project/visuel/img/Mute/0.png").convert_alpha()
        mixer_music.load(f"./Project/visuel/Audio/{i2}.ogg")

mute_music_button_on = Button(screen, width-74, 10, mute_sound_img, 64, 64)

mixer_music.set_volume(0.2)
mixer_music.play(loops=-1)

#for the restart and continue buttons
try:
	restart_button_img = image.load("./img/ResetBackground/0.png").convert_alpha()
except:
	try:
		restart_button_img = image.load("./visuel/img/ResetBackground/0.png").convert_alpha()
	except:
		restart_button_img = image.load("./Project/visuel/img/ResetBackground/0.png").convert_alpha()

restart_button = Button(screen, width/2 - 128, height - 74, restart_button_img, 256, 64)

#for the sound effect of the victory
class you_win():
	def __init__(self):
		try:
			mixer_music.load(f"./Audio/2.ogg")
		except:
			try:
				mixer_music.load(f"./visuel/Audio/2.ogg")
			except:
				mixer_music.load(f"./Project/visuel/Audio/2.ogg")
	
		mixer_music.set_volume(1)
		mixer_music.play()

#for the shop buttons:
try:
	close_shop_img = image.load("./img/Shop/0.png").convert_alpha()
	item_1_img = image.load("./img/Shop/1.png").convert_alpha()
	item_2_img = image.load("./img/Shop/2.png").convert_alpha()
	item_3_img = image.load("./img/Shop/3.png").convert_alpha()
	item_4_img = image.load("./img/Shop/4.png").convert_alpha()
	item_5_img = image.load("./img/Shop/5.png").convert_alpha()
	item_6_img = image.load("./img/Shop/6.png").convert_alpha()
except:
	try:
		close_shop_img = image.load("./visuel/img/Shop/0.png").convert_alpha()
		item_1_img = image.load("./visuel/img/Shop/1.png").convert_alpha()
		item_2_img = image.load("./visuel/img/Shop/2.png").convert_alpha()
		item_3_img = image.load("./visuel/img/Shop/3.png").convert_alpha()
		item_4_img = image.load("./visuel/img/Shop/4.png").convert_alpha()
		item_5_img = image.load("./visuel/img/Shop/5.png").convert_alpha()
		item_6_img = image.load("./visuel/img/Shop/6.png").convert_alpha()
	except:
		close_shop_img = image.load("./Project/visuel/img/Shop/0.png").convert_alpha()
		item_1_img = image.load("./Project/visuel/img/Shop/1.png").convert_alpha()
		item_2_img = image.load("./Project/visuel/img/Shop/2.png").convert_alpha()
		item_3_img = image.load("./Project/visuel/img/Shop/3.png").convert_alpha()
		item_4_img = image.load("./Project/visuel/img/Shop/4.png").convert_alpha()
		item_5_img = image.load("./Project/visuel/img/Shop/5.png").convert_alpha()
		item_6_img = image.load("./Project/visuel/img/Shop/6.png").convert_alpha()

close_shop_button = Button(screen, 20, 20, close_shop_img, 128, 128)
item_1_button = Button(screen, 764, 212, item_1_img, 128, 128)
item_2_button = Button(screen, 920, 212, item_2_img, 128, 128)
item_3_button = Button(screen, 1074, 212, item_3_img, 128, 128)
item_4_button = Button(screen, 764, 414, item_4_img, 128, 128)
item_5_button = Button(screen, 920, 414, item_5_img, 128, 128)
item_6_button = Button(screen, 1074, 414, item_6_img, 128, 128)