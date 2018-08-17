#Programme started le 3 juillet environ
#WATAFAKE CORPORATION FIRST GAME PROJECT


import pygame ,o
s
import time
from pygame.locals import *
import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)    #to show the icon even in the taskbar


folder = "Graphics\\"

pygame.init()
pygame.mixer.init()
pygame.mixer.pre_init()

#Colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
RED = ( 255, 0 , 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
GREY = (128, 128 ,128)
CYAN = ( 0 , 255, 255)



#Global variables
WIDTH = 1080
HEIGHT = 600
RESOLUTION = ( WIDTH , HEIGHT)
TITLE = "Killing Stalking 1.0 "
FPS = 15
clock = pygame.time.Clock()



icon_32x32 = pygame.image.load(folder+"icon.png")
pygame.display.set_icon(icon_32x32)



screen = pygame.display.set_mode(RESOLUTION)

pygame.display.set_caption(TITLE)

sound = pygame.mixer.Sound(folder+'MENU.wav')

pygame.mouse.set_visible(False)
#Loading images
bg0 = pygame.image.load(folder+"bg0.jpg")
bg1 = pygame.image.load(folder+"bg1.png")
cursor = pygame.image.load(folder+"cursor.png")
security_door = pygame.image.load(folder+"security_door.png")
yoonbum_hand = pygame.image.load(folder+"yoonbum_hand.png")





font_text = pygame.font.Font(folder+"IndieFlower.ttf",18)
font_text_small = pygame.font.Font(folder+"IndieFlower.ttf",15)
font_text_small1 = pygame.font.Font(folder+"IndieFlower.ttf",10)
font_name = pygame.font.Font(folder+"blowbrush.ttf",35)

font_title_chapter = pygame.font.Font(folder+"youmurdererbb_reg.ttf",100)
font_title_chapter1 = pygame.font.Font(folder+"youmurdererbb_reg.ttf",140)
font_current_chapter = pygame.font.Font(folder+"youmurdererbb_reg.ttf",37)

font1 = pygame.font.SysFont("Trebuchet MS", 5)
font2 = pygame.font.SysFont("trebuchetms", 15)
font3 = pygame.font.SysFont("trebuchetms",30)
font4 = pygame.font.SysFont("trebuchetms",20)
font_obj_num = pygame.font.SysFont("trebuchetms",12)

def message(msg, color,position,font):
	screen_txt = font.render(msg, True, color)
	screen.blit(screen_txt, position)


def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

STARTE = pygame.image.load(folder+"STARTENTER.png")
OPTIONSE = pygame.image.load(folder+"OPTIONSENTER.png")
LOADE = pygame.image.load(folder+"LOADENTER.png")
QUITE = pygame.image.load(folder+"QUITENTER.png")

START0 = pygame.image.load(folder+"START0.png")
START1 = pygame.image.load(folder+"START1.png")
START2 = pygame.image.load(folder+"START2.png")
START3 = pygame.image.load(folder+"START3.png")
START4 = pygame.image.load(folder+"START4.png")


OPTION0 =pygame.image.load(folder+"OPTIONS0.png")
OPTION1 =pygame.image.load(folder+"OPTIONS1.png")
OPTION2 =pygame.image.load(folder+"OPTIONS2.png")
OPTION3 =pygame.image.load(folder+"OPTIONS3.png")


LOAD0 =pygame.image.load(folder+"LOAD0.png")
LOAD1 =pygame.image.load(folder+"LOAD1.png")
LOAD2 =pygame.image.load(folder+"LOAD2.png")
LOAD3 =pygame.image.load(folder+"LOAD3.png")
LOAD4 =pygame.image.load(folder+"LOAD4.png")



QUIT0 =pygame.image.load(folder+"QUIT0.png")
QUIT1 =pygame.image.load(folder+"QUIT1.png")
QUIT2 =pygame.image.load(folder+"QUIT2.png")
QUIT3 =pygame.image.load(folder+"QUIT3.png")
QUIT4 =pygame.image.load(folder+"QUIT4.png")


darken_quit_background = pygame.image.load(folder+"darken_quit_background.png")
quit_label = pygame.image.load(folder+"quit_label.png")
yes_on = pygame.image.load(folder+"yes_on.png")
yes_off = pygame.image.load(folder+"yes_off.png")
no_on = pygame.image.load(folder+"no_on.png")
no_off = pygame.image.load(folder+"no_off.png")

def start_menu():

	pygame.mixer.Sound.play(sound)
	
	menu = True
	i = 0
	button_menu = 0
	n= 0
	k = 0
	po = 0
	sure_quit= False
	po_timer = False
	yes_selected = False
	no_selected = True


	bg1_x = 460
	bg1_speed = 1
	cte_ani_hand = 0
	yoonbum_hand_x = 690
	yoonbum_hand_y = 50
	yoonbum_hand_vx = 5
	yoonbum_hand_vy = 5

	key0 = False
	key1 = False
	key2 = False
	key3 = False
	

	while menu:
		mouse_position=pygame.mouse.get_pos()
		print(mouse_position)

		#Event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				menu = False
				pygame.quit()
				quit()


			if 13 < mouse_position[0] < 310 :
				if 346 < mouse_position[1] < 394:
					button_menu =0
					if event.type == MOUSEBUTTONDOWN:
						key0 = True
						print(key0)
				elif 406 < mouse_position[1] < 456:
					button_menu =1
					if event.type == MOUSEBUTTONDOWN:
						key1 = True
				elif 466 < mouse_position[1] < 506:
					button_menu =2
					if event.type == MOUSEBUTTONDOWN:
						key2 = True
				elif 516 < mouse_position[1] < 566:
					button_menu =3
					if event.type == MOUSEBUTTONDOWN:
						key3 = True
			if event.type == pygame.KEYDOWN  and not sure_quit:
				if event.key == pygame.K_UP and k < 0:
					n = 0
					if button_menu>0:
						button_menu -= 1
						k = 20
					else:
						button_menu = 3
						k = 20
				if event.key == pygame.K_DOWN and k < 0:
					n = 0
					if button_menu <3:
						button_menu += 1
						k = 20
					else :
						button_menu = 0
						k = 20

				

				
				if event.key == pygame.K_RETURN  and button_menu == 0:
					screen.blit(STARTE,(WIDTH/50,HEIGHT/1.5-HEIGHT/12))
					pygame.display.update()
					time.sleep(0.5)
					sound.stop()
					screen.fill(BLACK)
					pygame.display.update()
					time.sleep(2)
					start_game()

				if event.key == pygame.K_RETURN  and button_menu == 1:
					screen.blit(OPTIONSE,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+60))
					pygame.display.update()
					time.sleep(0.5)

				if event.key == pygame.K_RETURN  and button_menu == 2:
					screen.blit(LOADE,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+120))
					pygame.display.update()
					time.sleep(0.5)

				if event.key == pygame.K_RETURN  and button_menu == 3:
					screen.blit(QUITE,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+180))
					pygame.display.update()
					time.sleep(0.5)
					sure_quit = True 
					po_timer = True

				

			if event.type == pygame.KEYDOWN and sure_quit and po > 15:
				if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
					yes_selected = not yes_selected
					no_selected = not no_selected	
				if event.key == pygame.K_RETURN and yes_selected and sure_quit:
					menu = False
					

				elif event.key == pygame.K_RETURN and no_selected and sure_quit:
					sure_quit = False
					po= 0 	
					po_timer = False	

			if event.type == pygame.MOUSEBUTTONDOWN and not sure_quit:
				if key0  and button_menu == 0:
					screen.blit(STARTE,(WIDTH/50,HEIGHT/1.5-HEIGHT/12))
					pygame.display.update()
					time.sleep(0.5)
					sound.stop()
					screen.fill(BLACK)
					pygame.display.update()
					time.sleep(2)
					start_game()

				if key1 and button_menu == 1:
					screen.blit(OPTIONSE,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+60))
					pygame.display.update()
					time.sleep(0.5)

				if key2  and button_menu == 2:
					screen.blit(LOADE,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+120))
					pygame.display.update()
					time.sleep(0.5)

				if key3 and button_menu == 3:
					screen.blit(QUITE,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+180))
					pygame.display.update()
					time.sleep(0.5)
					sure_quit = True 
					po_timer = True



		k-= 3
		if po_timer:
			po += 5

		if po_timer > 15:
			po_timer = 0
		#DYNAMISM
		
		screen.blit(bg0,(0,0))
		screen.blit(bg1,(bg1_x,145))
		if bg1_x < 525:
			bg1_x += bg1_speed
		else:
			cte_ani_hand += 1 
			screen.blit(security_door,(700,50))
			if cte_ani_hand < 10:
				yoonbum_hand_vx = 0
				yoonbum_hand_vy = 0
			elif cte_ani_hand < 20:
				yoonbum_hand_vx = 2
				yoonbum_hand_vy = 1

			elif cte_ani_hand < 30:
				yoonbum_hand_vx = 0
				yoonbum_hand_vy = 0

			elif cte_ani_hand < 40:
				yoonbum_hand_vx = 3
				yoonbum_hand_vy = -1
			elif cte_ani_hand < 50:
				yoonbum_hand_vx = 0
				yoonbum_hand_vy = 0

			elif cte_ani_hand < 63:
				yoonbum_hand_vx = 0

				yoonbum_hand_vy = 2

			elif cte_ani_hand <75:
				yoonbum_hand_vx = 0

				yoonbum_hand_vy = 0

			elif cte_ani_hand <85:
				yoonbum_hand_vx = -5
				
				yoonbum_hand_vy = -3
				
			elif cte_ani_hand <95:
				yoonbum_hand_vx = 0

				yoonbum_hand_vy = 0
				yoonbum_hand_x = 690
				yoonbum_hand_y = 50
			elif cte_ani_hand>120:
				cte_ani_hand = 0






	

		

			screen.blit(yoonbum_hand, (yoonbum_hand_x,yoonbum_hand_y))
			yoonbum_hand_x+=yoonbum_hand_vx
			yoonbum_hand_y+=yoonbum_hand_vy


		#########################
		#Menu button
		#Start button









		



		screen.blit(START0,(WIDTH/50,HEIGHT/1.5-HEIGHT/12))
		screen.blit(OPTION0,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+60))
		screen.blit(LOAD0,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+120))
		screen.blit(QUIT0,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+180))

		if button_menu == 0:
			if n < 15:
				screen.blit(START0,(WIDTH/50,HEIGHT/1.5-HEIGHT/12))
			elif 15<= n < 30:
				screen.blit(START1,(WIDTH/50,HEIGHT/1.5-HEIGHT/12))
			elif 30<= n < 45:
				screen.blit(START2,(WIDTH/50,HEIGHT/1.5-HEIGHT/12))
			elif 45<= n < 60:
				screen.blit(START3,(WIDTH/50,HEIGHT/1.5-HEIGHT/12))
			elif 60<= n < 75:
				screen.blit(START4,(WIDTH/50,HEIGHT/1.5-HEIGHT/12))
			if n > 75:
				n = 0
			n+=5

		if button_menu ==1:
			if n < 15:
				screen.blit(OPTION0,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+60))
			elif 15<= n < 30:
				screen.blit(OPTION1,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+60))
			elif 30<= n < 45:
				screen.blit(OPTION2,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+60))
			elif 45<= n < 60:
				screen.blit(OPTION3,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+60))
			if n > 60:
				n = 0
			n+=5

		if button_menu == 2:
			if n < 15:
				screen.blit(LOAD0,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+120))
			elif 15<= n < 30:
				screen.blit(LOAD1,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+120))
			elif 30<= n < 45:
				screen.blit(LOAD2,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+120))
			elif 45<= n < 60:
				screen.blit(LOAD3,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+120))
			elif 60<= n < 75:
				screen.blit(LOAD4,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+120))
			if n > 75:
				n = 0
			n+=5


		if button_menu ==3:
			if n < 15:
				screen.blit(QUIT0,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+180))
			elif 15<= n < 30:
				screen.blit(QUIT1,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+180))
			elif 30<= n < 45:
				screen.blit(QUIT2,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+180))
			elif 45<= n < 60:
				screen.blit(QUIT3,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+180))
			elif 60<= n < 75:
				screen.blit(QUIT4,(WIDTH/50,HEIGHT/1.5-HEIGHT/12+180))
			if n > 75:
				n = 0
			n+=5

		if sure_quit:
			screen.blit(darken_quit_background,(0,0))
			screen.blit(quit_label , (90,50))
			if not yes_selected:
				screen.blit(yes_off , (405, 405))

			else:
				screen.blit(yes_on , (405, 405))

			if no_selected:
				screen.blit(no_on , (685,405))

			else:
				screen.blit(no_off , (685,405))


		message("Visual novel made by the twins Imane and Amine Elmouradi in 2017 on june.",GREY,(700,585),font1)
		#############################################
		#SOUND

		




	



		

		screen.blit(cursor,mouse_position)


		#########################
		pygame.display.update()
		clock.tick(FPS)




#intro animation
intro0 = pygame.image.load(folder+"intro0.png")
intro1 = pygame.image.load(folder+"intro1.png")
intro2 = pygame.image.load(folder+"intro2.png")
intro3 = pygame.image.load(folder+"intro3.png")
bg_cave0= pygame.image.load(folder+"cellar.png")


#game elements
barre = pygame.image.load(folder+"barre.png")

barre_hp = pygame.image.load(folder+"barre_hp.png")




yoonbum25o = pygame.image.load(folder+"yoonbum25o.png")
yoonbum25c = pygame.image.load(folder+"yoonbum25c.png")


img1 = yoonbum25o
img2 = yoonbum25c

yoonbum75o = pygame.image.load(folder+"yoonbum75o.png")
yoonbum75c = pygame.image.load(folder+"yoonbum75c.png")

yoonbum50o = pygame.image.load(folder+"yoonbum50o.png")
yoonbum50c = pygame.image.load(folder+"yoonbum50c.png")

yoonbum0 = pygame.image.load(folder+"yoonbum0.png")


sacmini = pygame.image.load(folder+"inventaire.png")
sacmaxi = pygame.image.load(folder+"inventaire_light.png")

inventaire_grand = pygame.image.load(folder+"inventaire_biggy.png")
inventory = pygame.image.load(folder+"InventaireINTERNE.png")




#interactive objects
boxes_hide_inside = pygame.image.load(folder+"boxes_hide_inside.png")
boxes_show_inside = pygame.image.load(folder+"boxes_show_inside.png")

box_hide = pygame.image.load(folder+"box_hide.png")
box_show = pygame.image.load(folder+"box_show.png")

sceau_rouge = pygame.image.load(folder+"sceau_rouge.png")
sceau_rouge_show = pygame.image.load(folder+"sceau_rouge_show.png")

etagere = pygame.image.load(folder+"etagere.png")


yoonbum_bed = pygame.image.load(folder+"yoonbum_bed.png")
barre_xp = pygame.image.load(folder+"barre_xp.png")



arrow_right_off = pygame.image.load(folder+"arrow_right_off.png")
arrow_right_on = pygame.image.load(folder+"arrow_right_on.png")

arrow_left_off = pygame.image.load(folder+"arrow_left_off.png")
arrow_left_on = pygame.image.load(folder+"arrow_left_on.png")
arrow_up_off = pygame.image.load(folder+"arrow_up_off.png")
arrow_up_on = pygame.image.load(folder+"arrow_up_on.png")

cellar = pygame.image.load(folder+"Cellar1.png")







sangwoo_smile = pygame.image.load(folder+"Sangwoo-smile.png")
sangwoo_talk = pygame.image.load(folder+"SangwooTalking.png")
sangwoo_angry = pygame.image.load(folder+"SangwooAngry.png")


#Variables
barre_height = 1080
barre_width = 150

yoonbum_height = 200
yoonbum_width = 180
intro_speech = ["You", "there !", "You","must", "know" ,"that" ,"everyone", "in" ,"his", "life" ,"time..." ,"lives", "at" ,"least...", "ONE" ,"NIGHTMARE" ,"and" ,"for", "you" ,"it's" ,"just" ,"starting" ,"right","now !"]



#PROFIL CHARACTER IMGS LOADING
profil_character = pygame.image.load(folder+"profil_character.png")







#Interactive objects images
apple = pygame.image.load(folder+"apple.png")
apple_for_details = pygame.image.load(folder+"apple_for_details.png")

knife = pygame.image.load(folder+"knife.png")
knife_for_details = pygame.image.load(folder+"knife_for_details.png")

bandage = pygame.image.load(folder+"bandage.png")
bandage_inv = pygame.image.load(folder+"bandage_inv.png")
bandage_selected_img = pygame.image.load(folder+"bandage_selected_img.png")
bandage_for_details = pygame.image.load(folder+"bandage_for_details.png")

key = pygame.image.load(folder+"key.png")
key_selected_img = pygame.image.load(folder+"key_selected.png")
key_inv = pygame.image.load(folder+"key_inv.png")
key_for_details = pygame.image.load(folder+"key_for_details.png")


banana = pygame.image.load(folder+"banana.png")
banana_selected_img = pygame.image.load(folder+"banana_selected.png")
banana_inv = pygame.image.load(folder+"banana_inv.png")
banana_for_details = pygame.image.load(folder+"banana_for_details.png")

bequille = pygame.image.load(folder+"bequille.png")
bequille_selected_img = pygame.image.load(folder+"bequille_selected.png")
bequille_inv = pygame.image.load(folder+"bequille_inv.png")



prologue = pygame.image.load(folder+"prologue.png")

next_img = pygame.image.load(folder+"next.png")

title_chapter = pygame.image.load(folder+"title_chapter.png")
current_chapter = pygame.image.load(folder+"current_chapter.png")

choice_label = pygame.image.load(folder+"choice_label.png")

sangwoo_cloth_1 = pygame.image.load(folder+"sangwoo_cloth1.png")

bloody_background = pygame.image.load(folder+"bloody_background.png")

yoonbum_menoter = pygame.image.load(folder+"yoonbum_menotte.png")
yoonbum_menotte_bloody = pygame.image.load(folder+"yoonbum_menotte_blood.png")

yoonbum_menoter1 = pygame.image.load(folder+"yoonbum_menotte1.png")
yoonbum_menoter2 = pygame.image.load(folder+"yoonbum_menotte2.png")
yoonbum_menoter3 = pygame.image.load(folder+"yoonbum_menotte3.png")
yoonbum_menoter4 = pygame.image.load(folder+"yoonbum_menotte4.png")
yoonbum_menoter5 = pygame.image.load(folder+"yoonbum_menotte5.png")

yoonbum_surprised1 = pygame.image.load(folder+"yoonbum_surprised1.png")
yoonbum_surprised2 = pygame.image.load(folder+"yoonbum_surprised2.png")
yoonbum_tired = pygame.image.load(folder+"yoonbum_tired.png")


yoonbum_sac_seen = pygame.image.load(folder+"yoonbum_sac_seen.png")
yoonbum_sac_seen1 = pygame.image.load(folder+"yoonbum_sac_seen1.png")



breath_img = pygame.image.load(folder+"breath.png")

wow_omg = pygame.image.load(folder+"WOW.png")
wow_omg1 = pygame.image.load(folder+"WOW1.png")


sangwoo_fist = pygame.image.load(folder+"sangwoo_fist.png")
sangwoo_fist1 = pygame.image.load(folder+"sangwoo_fist1.png")


small_arrow = pygame.image.load(folder+"small_arrow.png")
arrow_glowing_small = pygame.image.load(folder+"arrow_glowing_small.png")
pygame.mixer.music.load(folder+"scary_music.mp3")

fist_sound = pygame.mixer.Sound(folder+"Strong_Punch-Mike_Koenig-574430706.wav")

quests = pygame.image.load(folder+"quests.png")
quests_glow = pygame.image.load(folder+"quests_glow.png")
quests_open = pygame.image.load(folder+"quests_open.png")


arrow_right_small1 = pygame.image.load(folder+"arrow_right_small1.png")
arrow_right_small1_glow = pygame.image.load(folder+"arrow_right_small1_glow.png")
fist_sound = pygame.mixer.Sound(folder+"Strong_Punch-Mike_Koenig-574430706.wav")
def start_game():
	full_energy = False

	timer_energy_1 = 0
	timer_energy_2 = 0
	timer_energy_3 = 0
	timer_energy_4 = 0
	timer_energy_5 = 0







	

	apple_details_on = False
	knife_details_on = False
	bandage_details_on = False
	key_details_on = False
	banana_details_on = False





	start_game = True
	intro_working = True
	game_working = False





	sound0 = pygame.mixer.Sound(folder+"intro0.wav")
	
	

	x_off_set = 0
	y_off_set = 0
	arrow_left = False
	arrow_up = False
	arrow_right = False

	inventory_clicked = False
	inventory_big = False
	i =  0
	j = 0
	bg_tracker = 0
	k = 0

	show_bag = False
	show_arrow = False
	show_arrow_right = False
	show_arrow_left = False
	show_arrow_up = False

	show_yoonbum = True
	show_barre = True

	speech_tracker = 0 

	scene = 1
	x = - 1080
	x_change = 0
	xp_length = 0
	x_box = - 1000
	x_box2 = 460
	x_solo_box = 200
	x_sceau = 720
	x_bed = 200
	x_etagere = 650
	box_hide_inside = True
	boxes_hide = True
	boxes2_hide = True
	sceau_hide_inside = True


	apple_selected = False
	apple_taken = False

	knife_selected = False
	knife_taken = False


	bandage_taken = False
	bandage_selected = False

	key_taken = False
	key_selected = False


	banana_taken = False
	banana_selected = False

	bequille_selected = False
	bequille_taken = False

	l_objects_taken = []

	ani_close_eyes = 0

	profil_character_clicked = False
	show_profil = True


	timer = 0
	blocked = True

	barre_hp_lvl = 120



	#OBJECTS NUMBER
	apple_num = 1
	banana_num = 1
	knife_num = 1
	key_num = 1
	bandage_num = 1

	play = True


	apple_used = False
	bandage_used = False
	banana_used = False
	knife_used = False
	key_used = False


	logs = ""
	logs_color = GREEN

	list_object_def_inv = []

	x_prologue = -200
	speed_prologue = 45

	choice = 1
	choice1_selected = False
	choice2_selected = False

	i_hit_u = False
	next_hide = True
	next_selected = False
	back_selected = False


	cte_ani_menotte = 0 
	cte_ani_surprised = 0

	cte_ani_breath = 0

	x_yoonbum_tired = 1300
	yoonbum_tired_speed = 25

	talking = True
	cross_selected = False

	x_profil_set = 0
	y_profil_set = 0



	show_quests = False
	fist_ani = 0
	quests_selected = False
	quests_clicked = False

	cross_selected1 = False
	


	q1 = False
	q2 = False
	q3 = False
	q4 = False
	q5 = False
	q6 = False
	q7 = False
	q8 = False


	arrow_right_small1_glow_state = False
	page_quests = 0
	final_fist_ani  =0
	while start_game:


		mouse_position = pygame.mouse.get_pos()
		#print(mouse_position)
		#print(list_object_def_inv)
		#Event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				start_game = False
				pygame.quit()
				quit()

			if event.type == KEYDOWN:
				

				if event.key == pygame.K_SPACE:
					pygame.mixer.Sound.stop(sound0)
					intro_working = False
					game_working = True
				if event.key == pygame.K_LEFT:
					if xp_length >= 89*12:
						xp_length = 0
					xp_length += 89
					barre_hp_lvl -=15



			if 661 < mouse_position[0]-x_off_set < 671 and 65 < mouse_position[1]-y_off_set < 75:
				cross_selected = True
				if event.type == pygame.MOUSEBUTTONDOWN:
					inventory_clicked = False

			else:
				cross_selected = False

			if 662 < mouse_position[0] < 672 and 122 < mouse_position[1] < 134:
				cross_selected1 = True
				if event.type == pygame.MOUSEBUTTONDOWN:
					quests_clicked = False
			else:
				cross_selected1 = False

			if  11< mouse_position[0] < 60 and 60< mouse_position[1]< 90:
				inventory_big = True
				if event.type == pygame.MOUSEBUTTONDOWN:
					inventory_clicked = not inventory_clicked
					apple_details_on = False
					knife_details_on = False
					bandage_details_on = False
					key_details_on = False
					banana_details_on = False
					if speech_tracker ==6:
						speech_tracker +=1
			else:
				inventory_big = False
			

			if 32 < mouse_position[0] < 185 and 400 < mouse_position[1] < 557  :
				if event.type == pygame.MOUSEBUTTONDOWN:
					profil_character_clicked = not profil_character_clicked
			

			if 6 < mouse_position[0] < 	42 and 119 < mouse_position[1] < 160:
				quests_selected = True
				if event.type == pygame.MOUSEBUTTONDOWN:
					quests_clicked = True
					if speech_tracker == 36:
						speech_tracker += 1
			else:
				quests_selected = False


			if inventory_clicked:
				for obj_carac in list_object_def_inv:
					if obj_carac[0] < mouse_position[0] < obj_carac[1] and obj_carac[2] < mouse_position[1] < obj_carac[3]:
						if obj_carac[4]==1:
							apple_details_on = True
							knife_details_on = False
							bandage_details_on = False
							key_details_on = False
							banana_details_on = False
						elif  obj_carac[4]==2:
							apple_details_on = False
							knife_details_on = True
							bandage_details_on = False
							key_details_on = False
							banana_details_on = False
						elif  obj_carac[4]==3:
							apple_details_on = False
							knife_details_on = False
							bandage_details_on = True
							key_details_on = False
							banana_details_on = False
						elif  obj_carac[4]==4:
							apple_details_on = False
							knife_details_on = False
							bandage_details_on = False
							key_details_on = True
							banana_details_on = False
						elif  obj_carac[4]==5:
							apple_details_on = False
							knife_details_on = False
							bandage_details_on = False
							key_details_on = False
							banana_details_on = True
						

						
						if event.type == pygame.MOUSEBUTTONDOWN:
							if obj_carac[4]==1:
								apple_used = True
								if not full_energy:
									barre_hp_lvl -=15	
									timer = 0
									logs = "Vous avez recu 10 points de vie de \"Pomme\"."
									logs_color = GREEN
									l_objects_taken.remove((apple,1,apple_num))


									
									


							elif obj_carac[4]==2:
								knife_used = True
								
								timer = 0
								
							elif obj_carac[4]==3:
								bandage_used = True
								if barre_hp_lvl >=45:
									barre_hp_lvl-=45
									logs = "Vous avez recu 30 points de vie de \"Bandage\"."
									logs_color = GREEN
									timer = 0
									l_objects_taken.remove((bandage_inv,3,1))
									q4 = True
								print("BANDAGE")
							elif obj_carac[4]==4:
								key_used = True
								q2 = True
								l_objects_taken.remove((key_inv,4,1))
							elif obj_carac[4]==5:
								banana_used = True
								if not full_energy:
									logs = "Vous avez recu 10 points de vie de \"Banane\"."
									logs_color = GREEN
									timer = 0
									barre_hp_lvl-=15
									l_objects_taken.remove((banana_inv,5,1))
								
								
													 

			if 20 < mouse_position[0] < 150 and 300 < mouse_position[1] < 400 and show_arrow_left:
				arrow_left = True
				if event.type == pygame.MOUSEBUTTONDOWN:
					if scene == 1:
						x_change = 40
					show_bag = False
					show_arrow = False
					show_arrow_right = False
					show_arrow_left = False
					show_arrow_up = False
					show_yoonbum = False
				


	


			else:
				arrow_left = False

			if 800 < mouse_position[0] < 1000 and 20 < mouse_position[1]  <120 and show_arrow_up:
				arrow_up = True
				if event.type == pygame.MOUSEBUTTONDOWN :

					speech_tracker += 1
			else:
				arrow_up = False



			if 980 < mouse_position[0]< 1080 and 310 < mouse_position[1] < 400 and show_arrow_right:
				arrow_right = True
				if event.type == pygame.MOUSEBUTTONDOWN:
					if scene == 2:
						x_change = -40
					show_bag = False
					show_arrow = False
					show_arrow_right = False
					show_arrow_left = False
					show_arrow_up = False
					show_yoonbum = False
					
			else:
				arrow_right = False


			if 120< mouse_position[0] < 340 and 220 < mouse_position[1] < 380 and x_change == 0:
				boxes_hide = False
			else:
				boxes_hide = True

			if 230< mouse_position[0] < 450 and 250 < mouse_position[1] < 370 and x_change == 0:
				box_hide_inside = False
			else:
				box_hide_inside = True


			if barre_hp_lvl == 0:
				full_energy = True
			else:
				full_energy = False
			


			if 601 < mouse_position[0] < 631 and 298 < mouse_position[1] < 328:
				arrow_right_small1_glow_state = True
				if event.type == pygame.MOUSEBUTTONDOWN:
					page_quests += 1

			else:
				arrow_right_small1_glow_state = False


 
			print(mouse_position)
			print(barre_hp_lvl)

			if not show_barre and not inventory_clicked:
				if 320 < mouse_position[0] < 380 and 310 < mouse_position[1] < 350 and x_change == 0:
					apple_selected = True
					if event.type == pygame.MOUSEBUTTONDOWN:
						
						if not apple_taken and apple_num == 1:
							l_objects_taken.append((apple,1,apple_num))
							
							apple_taken = True
							q5 = True
						"""else:

							l_objects_taken.remove((apple,1,apple_num-1))
							
							l_objects_taken.append((apple,1,apple_num))
							apple_num += 1
							apple_taken = True"""
				else:
					apple_selected = False
						

				if 750 < mouse_position[0] < 930 and 270 < mouse_position[1] <  360 and x_change == 0:
					sceau_hide_inside = False
				else:
					sceau_hide_inside = True

				if 840 < mouse_position[0] < 930 and 300 < mouse_position[1] <  360 and x_change == 0:
					knife_selected = True
					if event.type == pygame.MOUSEBUTTONDOWN:
						if not knife_taken:
							l_objects_taken.append((knife,2,knife_num))
						knife_taken = True
						q6 = True
				else: knife_selected = False


				if 738 < mouse_position[0] < 822 and 170 < mouse_position[1] <225:
					bandage_selected = True
					if event.type == pygame.MOUSEBUTTONDOWN:
						if not bandage_taken:
							l_objects_taken.append((bandage_inv,3,bandage_num))
							bandage_selected = False
						bandage_taken = True
						q3 = True
				else: bandage_selected = False

				if 100 < mouse_position[0] < 135 and 126 < mouse_position[1] < 194:
		 			key_selected = True 
		 			if event.type == pygame.MOUSEBUTTONDOWN:
		 				if not key_taken:
		 					l_objects_taken.append((key_inv,4,key_num))
		 					key_selected = False
		 				key_taken = True
		 				q1 = True
				else: key_selected = False


				if 365 < mouse_position[0] < 430 and 300 < mouse_position[1] < 340 and scene==1:
		 			banana_selected = True 
		 			if event.type == pygame.MOUSEBUTTONDOWN:
		 				if not banana_taken:
		 					l_objects_taken.append((banana_inv,5,banana_num))
		 					banana_selected = False
		 				banana_taken = True
		 				q5 = True
				else: banana_selected = False

			if 295 < mouse_position[0] < 913 and 517<mouse_position[1]<545:
				choice1_selected = True
				if event.type == pygame.MOUSEBUTTONDOWN:
					choice =1
					speech_tracker += 1
					next_hide = False
			else:
				choice1_selected = False

			if 295 < mouse_position[0] < 913 and 556<mouse_position[1]<589:
				choice2_selected = True
				if event.type == pygame.MOUSEBUTTONDOWN:
					choice = 2
					speech_tracker += 1
					next_hide = False 
			else:
				choice2_selected = False


			
			if 979 < mouse_position[0] < 1059 and 555 < mouse_position[1] < 582 and not next_hide:
				next_selected = True
				if event.type == pygame.MOUSEBUTTONDOWN:
					speech_tracker += 1
			else:
				next_selected = False

			if 214 < mouse_position[0] < 288 and 555 < mouse_position[1] < 582 and not next_hide and speech_tracker>0:
				back_selected = True
				if event.type == pygame.MOUSEBUTTONDOWN:
					speech_tracker -= 1
			else:
				back_selected = False


		
		if intro_working:
			screen.blit(bg_cave0,(x,0))
			screen.blit(yoonbum_bed ,(x_bed , 350))
			screen.blit(boxes_hide_inside , (x_box,150))
			screen.blit(box_hide , (x_solo_box , 200))
			screen.blit(sceau_rouge , (x_sceau , 250 ))
			screen.blit(boxes_hide_inside , (x_box2,120))
			
			
			
			screen.blit(etagere,(x_etagere,0))
			screen.blit(bandage,(x_etagere+80,170))
			#############################################################################################################################
			if i< 225:
				screen.blit(intro0,(0,0))
			if 225 <= i <250:
				screen.blit(intro1,(0,0))
			elif 250<= i < 275:
				screen.blit(intro2,(0,0))
			elif 275<= i <300:
				screen.blit(intro1,(0,0))
			elif 300<= i <325:
				screen.blit(intro2,(0,0))
			elif 325<= i < 350:
				screen.blit(intro3,(0,0))
			
			elif 400<i<450:	
				screen.blit(title_chapter,(0,270))
				message("PROLOGUE",RED,(x_prologue,280),font_title_chapter)
				x_prologue+= speed_prologue
				if 412<i<430:
					speed_prologue = 0
				else:
					speed_prologue = 45

			if 225<i<400:
				sound1 = pygame.mixer.Sound(folder+"breath.wav")
				pygame.mixer.Sound.play(sound1)

			if i > 450:
				i = 0
				intro_working = False
				game_working = True

			i+= 1


		if intro_working:
			if k < 215:
				message("(Appuyez sur espace pour sauter)",GREY,(850,550),font_obj_num)
			if k==0:
				pygame.mixer.Sound.play(sound0)


			if k < 10:
				message(intro_speech[0],WHITE,(420,520),font2)

			elif 10< k < 25:
				message(" ".join(intro_speech[:2]),WHITE,(420,520),font2)


			elif 25< k < 30:
				message(" ".join(intro_speech[2:3]),WHITE,(250,520),font2)

			elif 30 < k < 35:
				message(" ".join(intro_speech[2:4]),WHITE,(250,520),font2)
			elif 35 < k < 40:
				message(" ".join(intro_speech[2:5]),WHITE,(250,520),font2)
			elif 40 < k < 45:
				message(" ".join(intro_speech[2:6]),WHITE,(250,520),font2)
			elif 45 < k < 50:
				message(" ".join(intro_speech[2:7]),WHITE,(250,520),font2)
			elif 55 < k < 60:
				message(" ".join(intro_speech[2:8]),WHITE,(250,520),font2)
			elif 60 < k < 62:
				message(" ".join(intro_speech[2:9]),WHITE,(250,520),font2)
			elif 62 < k < 64:
				message(" ".join(intro_speech[2:10]),WHITE,(250,520),font2)
			elif 64 < k < 75:
				message(" ".join(intro_speech[2:11]),WHITE,(250,520),font2)

			elif 76<k<78:
				message(" ".join(intro_speech[11:12]),WHITE,(420,520),font2)
			elif 80<k<82:
				message(" ".join(intro_speech[11:13]),WHITE,(420,520),font2)
			elif 84<k<110:
				message(" ".join(intro_speech[11:14]),WHITE,(420,520),font2)
			elif 110< k < 120:
				message("*Laughs*",WHITE,(420,520),font2)

			elif 120< k < 135:
				message(" ".join(intro_speech[14:15]),WHITE,(420,520),font2)
			elif 135 < k <160:
				message(" ".join(intro_speech[14:16]),WHITE,(420,520),font2)

			elif 162 < k < 164:
				message(" ".join(intro_speech[16:17]),WHITE,(420,520),font2)
			elif 164 < k< 166:
				message(" ".join(intro_speech[16:18]),WHITE,(420,520),font2)
			elif 166 < k < 180:
				message(" ".join(intro_speech[16:19]),WHITE,(420,520),font2)


			elif 180 < k < 182:
				message(" ".join(intro_speech[19:20]),WHITE,(380,520),font2)
			elif 182 < k < 184:
				message(" ".join(intro_speech[19:21]),WHITE,(380,520),font2)
			elif 184 < k < 186:
				message(" ".join(intro_speech[19:22]),WHITE,(380,520),font2)
			elif 186 < k < 188:
				message(" ".join(intro_speech[19:23]),WHITE,(380,520),font2)
			elif 190 < k < 215:
				message(" ".join(intro_speech[19:24]),WHITE,(380,520),font2)






		k+= 1

		x = x + x_change
		x_box += x_change
		x_sceau += x_change
		x_solo_box += x_change
		x_bed += x_change
		x_box2 += x_change
		x_etagere += x_change

		if scene == 1 and x >= 0 :
			x_change = 0


			show_bag = True
			show_arrow_left = False
			show_arrow_right = True
			show_arrow_up = True
			
			show_yoonbum = True
			scene = 2

		elif scene == 2 and x <= -1080:
			
			x_change = 0
			show_bag = True
			show_arrow_left = True
			show_arrow_right = False
			show_arrow_up = False
			
			show_yoonbum = True
			scene = 1 


		if game_working:
			if play:
				pygame.mixer.music.play(-1)
				play = False
			
			

			screen.blit(bg_cave0,(x,0))

			screen.blit(yoonbum_bed ,(x_bed , 350))
			pygame.draw.rect(screen, CYAN,[0,592,xp_length ,8])
			
			screen.blit(barre_xp , (0,592))
			screen.blit(etagere,(x_etagere,0))


			if not bandage_taken and (not bandage_selected or inventory_clicked or show_barre):
				screen.blit(bandage,(x_etagere+80,170))
			if bandage_selected and not bandage_taken and not inventory_clicked and not show_barre:
				screen.blit(bandage_selected_img,(x_etagere+80,170))

				message("Bandage",WHITE,(784,160),font2)


			if not key_taken and (not key_selected or inventory_clicked  or show_barre or speech_tracker ==36) :
				screen.blit(key,(x_bed-117,118))
			if key_selected and not key_taken and not inventory_clicked and not show_barre and speech_tracker >36:
				screen.blit(key_selected_img , (x_bed-117,118))
				message("Clé",WHITE,(x_bed-100,98),font2)




			if boxes_hide or inventory_clicked  or show_barre :
				screen.blit(boxes_hide_inside , (x_box,150))
			else:
				screen.blit(boxes_show_inside, (x_box,150))

			if box_hide_inside or  inventory_clicked  or show_barre :
				screen.blit(box_hide , (x_solo_box , 200))
				
			else:
				if not apple_taken:
					screen.blit(apple,(x_solo_box+130,300))

				if not banana_taken and scene == 1:
					screen.blit(banana,(365+x_change,300))
				screen.blit(box_show , (x_solo_box , 200))
				if apple_selected and not apple_taken:
					screen.blit(apple,(x_solo_box+130,300))
					message("Pomme",WHITE,(x_solo_box+130,280),font2)
				
				
				if banana_selected and not banana_taken and scene==1:
					screen.blit(banana,(365+x_change,300))
					message("Banane",WHITE,(365+x_change,280),font2)


			
			if sceau_hide_inside or inventory_clicked  or show_barre:
				screen.blit(sceau_rouge , (x_sceau , 250 ))
			else:
				if not knife_taken:
					screen.blit(knife,(x_sceau+122 , 310))
				screen.blit(sceau_rouge_show , ( x_sceau , 250))
				if knife_selected and not knife_taken:
					screen.blit(knife , (x_sceau+122 , 310))
					#pygame.draw.rect(screen,BLACK,[x_sceau+122,290,20,10])
					message("Couteau",WHITE,(x_sceau+122,290),font2)

				


			if boxes2_hide or inventory_clicked  or show_barre:
				screen.blit(boxes_hide_inside , (x_box2,120))
			else:
					
				screen.blit(boxes_show_inside, (x_box2,120))



			if show_arrow_left and not inventory_clicked and not show_barre:
				if not arrow_left :
					screen.blit(arrow_left_off ,(20, 300))
				else:
					screen.blit(arrow_left_on ,(20, 300))

			if show_arrow_up and not inventory_clicked and not show_barre :

				if not arrow_up :
						screen.blit(arrow_up_off ,(800, 20))
				else:
					screen.blit(arrow_up_on , (800,20))
								

			if show_arrow_right and not inventory_clicked and not show_barre :
				if not arrow_right :
						screen.blit(arrow_right_off ,(980, 310))
				else:
					screen.blit(arrow_right_on , (980,310))
				













































			if speech_tracker <= 5:


				if speech_tracker >= 4:
					if cte_ani_surprised% 10>5:

						screen.blit(yoonbum_sac_seen ,(720,100))

					else:
						screen.blit(yoonbum_sac_seen1 ,( 720,100))




				if speech_tracker>=0:
					
					screen.blit(yoonbum_tired,(x_yoonbum_tired,100))


				if x_yoonbum_tired < 500 :
					yoonbum_tired_speed = 0

				x_yoonbum_tired -= yoonbum_tired_speed

			

				if speech_tracker >= 2:
					cte_ani_surprised += 1 
					if cte_ani_surprised>20:
						if  cte_ani_surprised %20==0:
							screen.blit(yoonbum_surprised2,(475,320))
						else :
							screen.blit(yoonbum_surprised1,(475,320))



				if speech_tracker >= 1:
					cte_ani_menotte += 3 
				
					if  cte_ani_menotte < 10:
						screen.blit(yoonbum_menoter1,(20,100))
					elif cte_ani_menotte <20:
						screen.blit(yoonbum_menoter2,(20,100))
					elif cte_ani_menotte <30:
						screen.blit(yoonbum_menoter3,(20,100))
					elif cte_ani_menotte <40:
						screen.blit(yoonbum_menoter4,(20,100))

					elif cte_ani_menotte <50:
						screen.blit(yoonbum_menoter5,(20,100))

					elif 40<cte_ani_menotte :
							screen.blit(yoonbum_menoter,(20,100))
							if speech_tracker >=5:
								screen.blit(yoonbum_menotte_bloody,(20,100))

				if speech_tracker >=2:
					cte_ani_breath += 1

					if cte_ani_breath < 30:
						screen.blit(breath_img,(400,100))

					elif 30 <cte_ani_breath < 60:
						screen.blit(breath_img,(508,267))

					elif 60< cte_ani_breath < 90:
						screen.blit(breath_img,(420,350))

					elif 90< cte_ani_breath < 120:
						screen.blit(breath_img,(680,250))
					elif cte_ani_breath>120:
						cte_ani_breath = 0





			if speech_tracker==6:
				cte_ani_surprised+=1
				if cte_ani_surprised%10>5:
					screen.blit(wow_omg,(310,-10))
					screen.blit(arrow_glowing_small,(60,50))
				else:
					screen.blit(wow_omg1,(310,-10))
					screen.blit(small_arrow,(90,50))
				screen.blit(inventaire_grand,(490,160))


			if speech_tracker==36:
				cte_ani_surprised+=1
				if cte_ani_surprised%10>5:
					
					screen.blit(arrow_glowing_small,(60,120))
				else:
					
					screen.blit(small_arrow,(90,120))
				










			

				


			

			if speech_tracker == 13:
				screen.blit(sangwoo_smile,(450,100))


			if 13 < speech_tracker <= 14 or 35 >=speech_tracker>= 15 :
				if speech_tracker%2!=0:
					screen.blit(sangwoo_talk,(450,100))
				else:
					screen.blit(sangwoo_smile,(450,100))

			
			if (speech_tracker == 15 and choice==1) or speech_tracker>=38:
				screen.blit(sangwoo_angry,(450,100))
			if 35>=speech_tracker >=13 or speech_tracker>=38:
				screen.blit(sangwoo_cloth_1,(450,100))


			if show_barre:
				screen.blit(barre,(0,HEIGHT-barre_width))

			if show_yoonbum:
				screen.blit(barre_hp,(0,400))
				pygame.draw.rect(screen,BLACK,[8,417,22,barre_hp_lvl])
				if  150 - barre_hp_lvl >= 105:
					img1 = yoonbum75o
					img2 = yoonbum75c

				elif  150-barre_hp_lvl >=75:
					img1 = yoonbum50o
					img2 = yoonbum50c
				elif  150-barre_hp_lvl >0: 
					img1 = yoonbum25o
					img2 = yoonbum25c

				else:
					img1 = yoonbum0
					img2 = yoonbum0



					
				screen.blit(img1,(0,HEIGHT-yoonbum_width-20))
				if ani_close_eyes > 30:
					screen.blit(img2,(0,HEIGHT-yoonbum_width-20))
			if ani_close_eyes > 32:
				ani_close_eyes = 0

			ani_close_eyes += 1
			if show_bag:
				if inventory_big or inventory_clicked:
					screen.blit(sacmaxi , (10, 50))
				else:
					screen.blit(sacmini , (10, 50))


			
			
				



				
			if timer_energy_1!=0 or timer_energy_2!=0 or timer_energy_3!=0 or timer_energy_4!=0 or timer_energy_5!=0 :
				blocked = True
			else:
				blocked = False

			"""if full_energy and timer_energy < 30 and banana_used:
				message("Je devrai plutôt le garder pour plus tard.",WHITE,(420,20),font2)
				timer_energy+=1
			else:
				banana_used = False
				timer_energy = 0

			if full_energy and timer_energy < 30 and key_used:
				message("Il n'y a rien à ouvrir par ici.",WHITE,(420,20),font2)
				timer_energy+=1
			else:
				key_used = False
				timer_energy = 0

			if full_energy and timer_energy < 30 and bandage_used:
				message("Je n'ai aucune blessure grave.",WHITE,(420,20),font2)
				timer_energy+=1
			else:
				bandage_used = False
				timer_energy = 0"""


			

			

			if  profil_character_clicked:
				x_off_set = 290
				y_off_set = -30
			else:
				x_off_set = 0
				y_off_set = 0



									
				
			
		

			if show_barre and not next_hide:				
				#message(">>Next", RED , (960,550),font3)
				screen.blit(next_img,(980,555))
				if speech_tracker>0:
					screen.blit(next_img,(220,555)) 
				if not next_selected or inventory_clicked:
					message("Next",RED,(995,552),font_text)
				else:
					message("Next",WHITE,(995,552),font_text)
				if speech_tracker>0:
					if not back_selected or inventory_clicked:
						message("Back",RED,(225,552),font_text)
					else:
						message("Back",WHITE,(225,552),font_text)



			if speech_tracker == 0 :
				message("YOONBUM",BLUE, (260,465),font_name)
				if j > 45:
					next_hide = False
					message("Ughh...Ma tête me fait atrocement mal. Je n'arrive pas ",BLACK, (450,455),font_text)
					message("à bouger, mes muscles doivent être endommagés...",BLACK, (450,480),font_text)
			elif speech_tracker == 1:
				next_hide = False
				message("YOONBUM",BLUE, (260,465),font_name)
				message("Mais que- ? Je suis menotté ! Mais qu'est ce qui s'est ",BLACK, (450,455),font_text)
				message("passé bon sang ?! Où suis-je ?",BLACK, (450,480),font_text)
			elif speech_tracker == 2 :
				next_hide = False
				message("YOONBUM",BLUE, (260,465),font_name)
				message("Oh mais quelle est cette chose sous la table ?",BLACK, (450,455),font_text)
			elif speech_tracker == 3:
				next_hide = False
				message("YOONBUM",BLUE, (260,465),font_name)
				message("Ma vue ne s'est pas encore stabilisée.",BLACK,(450,455),font_text)
			elif speech_tracker == 4:
				message("YOONBUM",BLUE, (260,465),font_name)
				message("Ah, c'est mon sac! Il y'a peut-être mon téléphone là-dedans!",BLACK,(450,455),font_text)
				message("Je pourrai appelé de l'aide!",BLACK,(450,480),font_text)
				
			elif speech_tracker == 5:
				message("YOONBUM",BLUE, (260,465),font_name)
				message("Je peux l'atteindre si je m'étire assez... Juste un peu...",BLACK, (450,455),font_text)
				message("Aïe, j'ai trop forcé, mes poignés saignent du coup...",BLACK, (450,480),font_text)
			elif speech_tracker == 6:
				message("YOONBUM",BLUE,(260,465),font_name)
				message("A-A-A BINGO!",BLACK,(450,455),font_text)
				message("Vous disposez maintenant d'un inventaire.",GREY,(450,480),font2)
				message("(Cliquez dessus pour l'ouvrir.)",GREY,(490,500),font2)
				show_bag = True

			elif speech_tracker == 7:
				message("YOONBUM",BLUE, (260,465),font_name)
				message("Erf... Il est complètement vide....Bon... ce n'est pas grave,",BLACK,(450,455),font_text)
				message("je pourrai l'utiliser pour stocker des objets par la suite.",BLACK,(450,480),font_text)
				

			elif speech_tracker == 8:
				message("YOONBUM",BLUE, (260,465),font_name)
				message("*Sniff* *Sniff* C'est quoi cette odeur ?! *Tourne la tête* " ,BLACK,(450,470),font_text)
				
				

			

			elif speech_tracker ==9:
				message("YOONBUM",BLUE, (260,465),font_name)
				message("AA-HH Que vois-je ?! C'est bien un cadavre que je vois là ?!" ,BLACK,(450,455),font_text)
				message("Je dois sortir d'ici , je ne sais même pas ce qui m'attend ici." ,BLACK,(450,480),font_text)




			elif speech_tracker ==10:
				message("YOONBUM",BLUE, (260,465),font_name)
				message("Nous allons surement faire face à un tueur en série... " ,BLACK,(450,455),font_text)
				message("Ce qui ne m'enchante pas du tout." ,BLACK,(450,480),font_text)

			elif speech_tracker ==11:
				message("YOONBUM",BLUE, (260,465),font_name)
				message("J'ai du mal à respirer, SORTEZ-MOI DE LAAAA! AU SECOURS!!!! " ,BLACK,(450,455),font_text)
				message(" Arghhh... je suis à bout de souffle." ,BLACK,(450,480),font_text)

			elif speech_tracker == 12:
				message("YOONBUM",BLUE, (260,465),font_name)
				message("D-d-des bruits de pas... Quelqu'un ar-r-rive....! " ,BLACK,(450,455),font_text)
				
			elif speech_tracker == 13:
				message("SANGWOO",RED, (260,465),font_name)
				message("Bien le bonjour, t'en as fait du bruit toi! Tu sais que je" ,BLACK,(450,455),font_text)
				message(" peux tout entendre! ",BLACK,(450,480),font_text)

			elif speech_tracker == 14:
				next_hide = True
				message("SANGWOO",RED, (260,465),font_name)
				message("Quelque chose ne va pas ?" ,BLACK,(450,455),font_text)
				screen.blit(choice_label,(295,515))
				screen.blit(choice_label,(295,555))
				message("S-sangwoo? C'est toi qui es derrière tout ça ?" ,BLACK,(380,555),font_text)
				message("Espèce d'assassin! Que veux-tu de moi?! Laisse-moi sortir!!!" ,BLACK,(300,515),font_text)
				if choice2_selected :
					message("S-sangwoo? C'est toi qui es derrière tout ça ?" ,BLUE,(380,555),font_text)
				if choice1_selected:
					message("Espèce d'assassin! Que veux-tu de moi?! Laisse-moi sortir!!!" ,BLUE,(300,515),font_text)



			elif speech_tracker == 15 and choice==2:
				message("SANGWOO",RED, (260,465),font_name)
				message("Bein voyons! T'as vu une autre personne ici, peut-être?" ,BLACK,(450,455),font_text)
			

			elif speech_tracker==15 and choice ==1:
				message("SANGWOO",RED, (260,465),font_name)
				message("Hahaha... Où sont passées les bonnes manières, voyons?" ,BLACK,(450,455),font_text)
				message("Tu as oublié un détail. C'est MOI qui donne des ordres ici!" ,BLACK,(450,480),font_text)
				fist_ani += 1
				if fist_ani > 10:
					if fist_ani < 15:
						screen.blit(sangwoo_fist ,( 200,120))
					elif fist_ani < 20:
						screen.blit(sangwoo_fist1 ,( 200,120))
					elif fist_ani < 25:
						screen.blit(sangwoo_fist ,( 200,120))
					elif fist_ani < 30:
						screen.blit(sangwoo_fist1 ,( 200,120))
					elif fist_ani < 35:
						screen.blit(sangwoo_fist ,( 200,120))


				if not i_hit_u:
					
					pygame.mixer.Sound.play(fist_sound)
					barre_hp_lvl += 15
					i_hit_u = True


			elif speech_tracker == 16:
				message("YOONBUM",BLUE, (260,465),font_name)
				message("Je n'en crois pas mex yeux... Et ce cadavre derrière ... ?" ,BLACK,(450,455),font_text)
				
			elif speech_tracker == 17:
				message("SANGWOO",RED, (260,465),font_name)
				message("Oh elle, c'est juste la fille d'un CEO qui me prenait toujours " ,BLACK,(450,455),font_text)
				message("de haut, alors je me suis gentiment vengé." ,BLACK,(450,480),font_text)

			elif speech_tracker == 18:
				message("YOONBUM",BLUE, (260,465),font_name)
				message("(Gentiment ?	Tous ses membres ont été déchiquetés..." ,BLUE,(450,455),font_text)
				message("Ca sera surement mon tour dans pas très longtemps...)" ,BLUE,(450,480),font_text)

			elif speech_tracker == 19:
				message("YOONBUM",BLUE, (260,465),font_name)
				message("( Je dois trouver un moyen de sortir d'ici et au plus vite! )" ,BLUE,(450,455),font_text)
				
			elif speech_tracker == 20:
				message("SANGWOO",RED, (260,465),font_name)
				message(" Pourquoi as-tu l'air si angoissé ? N'es-tu pas venu de tes " ,BLACK,(450,455),font_text)
				message("propres moyens jusqu'à moi? A toi de payer le prix." ,BLACK,(450,480),font_text)


			elif speech_tracker == 21:
				message("YOONBUM",BLUE, (260,465),font_name)
				message("( Je ne pensais pas que c'était un criminel, j'étais loin" ,BLUE,(450,455),font_text)
				message("d'imaginer qu'il serait capable de telles choses infâmes.)" ,BLUE,(450,480),font_text)


			elif speech_tracker == 22:
				message("YOONBUM",BLUE, (260,465),font_name)
				message("\"Quand j'y pense, on était dans la même université. Je ne lui avais jamais " ,BLUE,(450,455),font_text_small)
				message(" adressé la parole, mais sa popularité et le nombre de personnes qui " ,BLUE,(450,475),font_text_small)
				message("l'entouraient portaient à croire que c'était un élève modèle,et d'une sympathie absolue. Pourtant... " ,BLUE,(218,495),font_text_small)
				message(" En regardant ses yeux en ce moment, je ne peux que sentir la haine, la cruauté et l'indifférence... " ,BLUE,(218,515),font_text_small)
				message("Mais où est passé le Sangwoo attentionné et angélique que nous connaissions tous ?! \"" ,BLUE,(218,535),font_text_small)
				message("" ,BLACK,(218,520),font_text_small)

			elif speech_tracker == 23:
				next_hide = True
				message("SANGWOO",RED, (260,465),font_name)
				message("Qu'y a-t-il ? Pourquoi es-tu si silencieux ? " ,BLACK,(450,455),font_text)
				message("Je ne t'ai pas égorgé pourtant, ou du moins pas encore..." ,BLACK,(450,480),font_text)

				screen.blit(choice_label,(295,515))
				screen.blit(choice_label,(295,555))

				message("Qu'est ce que tu veux de moi ?" ,BLACK,(460,555),font_text)
				message("Peux-tu m'épargner je t'en prie..." ,BLACK,(450,515),font_text)
				if choice1_selected:
					message("Peux-tu m'épargner je t'en prie..." ,BLUE,(450,515),font_text)
				if choice2_selected:
					message("Qu'est ce que tu veux de moi ?" ,BLUE,(460,555),font_text)


			elif speech_tracker == 24:
				next_hide = False
				message("SANGWOO",RED, (260,465),font_name)
				message(" Ahahah... Ca me donne un plaisir fou de voir mes victimes." ,BLACK,(450,455),font_text)

				message("s'appitoyer sur leur sort de cette manière." ,BLACK,(450,480),font_text)

			elif speech_tracker == 25 :
				message("SANGWOO",RED, (250,470),font_name)
				
				message("Je suis sur que je ne me lasserai jamais tant " ,BLACK,(450,455),font_text)
				message("que tu me tiendra compagnie." ,BLACK,(450,480),font_text)

			elif speech_tracker == 26 :
				message("SANGWOO",RED, (250,470),font_name)
				message("Alors prépare-toi à rester ici, pour le restant de tes jours! " ,BLACK,(450,455),font_text)
				
				

			elif speech_tracker == 27 :
				message("SANGWOO",BLUE, (260,465),font_name)
				message("Allons, trève de bavardage, prends cette boîte de conserve. Et bouffe  " ,BLACK,(450,455),font_text_small)
				message("tant que tu peux. Aujourd'hui je suis de bonne humeur, alors ne me gâche " ,BLACK,(450,475),font_text_small)
				message("pas ma journée. T'as vu à quel point t'es maigre ? Tu seras incapable de supporter les punitions " ,BLACK,(218,495),font_text_small)
				message("et les méthodes de torture que j'ai préparé spécialement pour toi. Bizarrement quand je vois des  " ,BLACK,(218,515),font_text_small)
				message("personnes aussi faibles que toi, ça me donne envie de les maltraiter et les martyriser." ,BLACK,(218,535),font_text_small)
				message("" ,BLACK,(218,520),font_text_small)
			elif speech_tracker ==28 :
				message("YOONBUM",BLUE, (250,470),font_name)
				message("(Cet homme est fou! Je dois agir exactement comme " ,BLUE,(450,455),font_text)
				message("il l'ordonne, si je tiens à survivre dans cet enfer...)",BLUE,(450,480),font_text)

			elif speech_tracker == 29 :
				message("YOONBUM",BLUE, (250,470),font_name)
				message("Je te remercie pour le repas... " ,BLACK,(450,455),font_text)
				
				message("Mais je ne peux pas le manger ainsi..." ,BLACK,(450,480),font_text)

			elif speech_tracker == 30 :
				message("SANGWOO",RED, (250,470),font_name)
				message("Oh j'avais complètement oublié que tu étais encore attaché " ,BLACK,(450,455),font_text)
				
				message("mais ce n'est pas grave,tu n'auras pas besoin de tes mains." ,BLACK,(450,480),font_text)

			elif speech_tracker == 31 :
				message("YOONBUM",BLUE, (250,470),font_name)
				message("Pardon ?" ,BLACK,(450,455),font_text)
				
				
			elif speech_tracker == 32 :
				message("SANGWOO",RED, (250,470),font_name)
				message("Eh oui, les chiens n'utilisent pas leurs pattes pour manger " ,BLACK,(450,455),font_text)
				
				message("mais leur gueule." ,BLACK,(450,480),font_text)

			elif speech_tracker == 33 :
				message("SANGWOO",RED, (250,470),font_name)
				message("Mais qu'est ce que tu attends ?  " ,BLACK,(450,455),font_text)

			elif speech_tracker == 34 :
				message("YOONBUM",BLUE, (250,470),font_name)
				message("( Il ne mentait pas quand il disait qu'il me prenait pour un " ,BLUE,(450,455),font_text)
				
				message("chien ...)" ,BLUE,(450,480),font_text)

			elif speech_tracker == 35 :
				message("YOONBUM",BLUE, (250,470),font_name)
				message("(Je ne peux pas supporter celà Mais je dois resister," ,BLUE,(450,455),font_text)
				message("il le faut! Si je tiens ne serait-ce qu'un millième à ma peau.)" ,BLUE,(450,480),font_text)
			elif speech_tracker == 36:
				show_barre = False
				show_quests = True
				show_bag = True
				next_hide = True


				message("Vous avez reçu  une nouvelle quête !", BLACK ,(300,80), font3)
				message("Cliquez sur votre journal de quête pour plus d'information!", BLACK,(200,125),font3)

			elif speech_tracker == 38:
				next_hide = False
				show_barre = True
				message("SANGWOO",RED, (250,470),font_name)
				message("Tu comptais partir ? " ,BLACK,(450,455),font_text)
				
			elif speech_tracker ==39:
				message("YOONBUM",BLUE, (250,470),font_name)
				message("Non pas du tout... " ,BLUE,(450,455),font_text)
				
			elif speech_tracker == 40:
				message("SANGWOO",RED, (250,470),font_name)
				message("Mais oui c'est ça , je devrai me débarasser de toi!" ,BLACK,(450,455),font_text)
				final_fist_ani+=1
				next_hide = True
				if barre_hp_lvl <=150:
					barre_hp_lvl+= 1
				if 20>final_fist_ani > 10:
					screen.blit(sangwoo_fist ,( 200,120))

				if 30>final_fist_ani > 20:
					screen.blit(sangwoo_fist ,( 100,250))

				if 40>final_fist_ani > 30:
					screen.blit(sangwoo_fist ,( 200,50))
					screen.blit(darken_quit_background,(0,0))

				if 50>final_fist_ani > 40:
					screen.blit(sangwoo_fist ,( 500,60))
					screen.blit(darken_quit_background,(0,0))

				if 60 >final_fist_ani > 50:
					screen.blit(sangwoo_fist ,(20,60))
					screen.blit(darken_quit_background,(0,0))

				if 70 >final_fist_ani > 60:
					screen.blit(sangwoo_fist ,(600,200))
					screen.blit(darken_quit_background,(0,0))

				if 140>final_fist_ani > 70:
					screen.blit(darken_quit_background,(0,0))
					message("GAME OVER",RED,(350,270),font_title_chapter1)

				if final_fist_ani == 10:
					pygame.mixer.Sound.play(fist_sound)

				if final_fist_ani == 15:
					pygame.mixer.Sound.play(fist_sound)
				if final_fist_ani == 20:
					pygame.mixer.Sound.play(fist_sound)

				if final_fist_ani == 25:
					pygame.mixer.Sound.play(fist_sound)

				if final_fist_ani == 30:
					pygame.mixer.Sound.play(fist_sound)

				if final_fist_ani == 40:
					pygame.mixer.Sound.play(fist_sound)




				if final_fist_ani>140:
					pygame.draw.rect(screen,BLACK,(0,0,WIDTH,HEIGHT))
					message("Merci d'avoir jouer , j'espere que ca vous a plu .",RED,(180,100),font_current_chapter)
					message("Je vous rassure ce n'est pas la vrai fin du jeu , il y'aura plus de contenu.",RED,(180,130),font_current_chapter)

				
				if final_fist_ani>180:
					
					message("Ce jeu a ete creer par les deux jumeaux Amine et Imane Elmouradi. ",RED,(130,160),font_current_chapter)
					message("Amine s'est charge de la programmation alors que Imane du design et du gameplay.",RED,(130,190),font_current_chapter)


				if final_fist_ani>220:
					
					message("Je tiens a remercier nos parents , nos professeurs et les eleves de notre classe a salmane.",RED,(130,220),font_current_chapter)
					message("On attend avec impatience vos feedbacks",RED,(130,250),font_current_chapter)
					message("sur cet email : amine_elmouradi@outlook.fr",RED,(130,280),font_current_chapter)

				if final_fist_ani>240:
					message("Cordialement",BLUE,(700,500),font_current_chapter)
					message("Elmouradi",BLUE,(720,530),font_current_chapter)


					



				
			





				


			if show_quests and show_bag and speech_tracker <39:
				if not quests_selected :
					screen.blit(quests,(10,120))
				else:
					screen.blit(quests_glow , (10, 120))










			elif speech_tracker >=50:
				show_barre = False


			if barre_hp_lvl >=135:
				screen.blit(bloody_background,(0,0))
			if speech_tracker<39:
				screen.blit(current_chapter,(0,0))
				message(" 0 prologue", RED ,(4,4),font_current_chapter)

			if show_bag:
				

				if inventory_clicked:
					km =0
					ind= 0
					ks = 0
					kd = 0
					list_object_def_inv = []
					if not profil_character_clicked:
						screen.blit(darken_quit_background, (0,0))
						screen.blit(inventory, ( 380, 70))
						pygame.draw.rect(screen,RED,[ 380 +inventory.get_width()-10,70,10,10])
						if not cross_selected:
							message('x',BLACK, (380 +inventory.get_width()-8,64),font2)
						else:
							message('x',WHITE, (380 +inventory.get_width()-8,64),font2)

						message('0,00 ',BLACK,(627,507),font2)


					## HERE WE BLIT OUR ITEMS PICKED BY THE USER
						for obj in l_objects_taken:
							screen.blit(obj[0],(390+km,90+ks))
							
							kd = km
							km+=obj[0].get_width()
							list_object_def_inv += [(390+kd,390+km,90+ks,150+ks,obj[1])]
							pygame.draw.rect(screen,BLACK,[390+kd,90+ks,15,15])
							l_numbers_obj = [(390+kd,90+ks),obj[2]]
							message(str(obj[2]),WHITE, (392+kd,92+ks),font_obj_num)

							ind+= 1

							if ind>=5:
								ks+=60
								km = 0
								kd = 0
								ind = 0


							#L'algorithme pour que le programme puisse reconnaitre les objets dans l'inventaire
							#Le principe est simple il y'aura une liste qui va stocker les coordonné qui délimite 
							#l'objet dans l'inventaire qui sera procedé dans la phase d'evenement de la souris et il
							# yaura un numero de série de l'objet
					else:
						
						kd = 0
						km = 0
						ks =0
						ind = 0
						for obj in l_objects_taken:

							screen.blit(obj[0],(680+km,65+ks))
							
							kd = km
							km+=obj[0].get_width()
							list_object_def_inv += [(680+kd,680+km,65+ks,125+ks,obj[1])]
							pygame.draw.rect(screen,BLACK,[680+kd,65+ks,15,15])
							l_numbers_obj = [(680+kd,65+ks),obj[2]]
							message(str(obj[2]),WHITE, (682+kd,67+ks),font_obj_num)

							ind+= 1

							if ind>=5:
								ks+=60
								km = 0
								kd = 0
								ind = 0

			j+=1

			if show_profil:
				if profil_character_clicked and not inventory_clicked:
					screen.blit(darken_quit_background, (0,0))
					screen.blit(profil_character,(300,45))

				if profil_character_clicked and  inventory_clicked:
					screen.blit(darken_quit_background, (0,0))
					screen.blit(profil_character,(170,45))
					screen.blit(inventory, (670, 45))
					pygame.draw.rect(screen,RED,[ 380 +inventory.get_width()-10+x_off_set,70+y_off_set,10,10])
					if not cross_selected:
						message('x',BLACK, (380 +inventory.get_width()-8+x_off_set,64+y_off_set),font2)
					else:
						message('x',WHITE, (380 +inventory.get_width()-8+x_off_set,64+y_off_set),font2)


					message('0,00 ',BLACK,(627+x_off_set,507+y_off_set),font2)


			if inventory_clicked:
				if apple_details_on:

					

					screen.blit(apple_for_details,(384+x_off_set,414+y_off_set))
					message("Il s'agit d'une pomme rouge.",BLACK,(486+x_off_set,424+y_off_set),font2)
					message("Redonne 10 points de vie.",BLACK,(486+x_off_set,440+y_off_set),font2)
					message("(Cliquez dessus pour l'utiliser.)",GREY,(500+x_off_set,480+y_off_set),font_obj_num)

				elif knife_details_on:
					screen.blit(knife_for_details,(384+x_off_set,414+y_off_set))
					message("Un couteau très aiguisé.",BLACK,(486+x_off_set,424+y_off_set),font2)
					message("Il y'a du sang dessus.",BLACK,(486+x_off_set,440+y_off_set),font2)
					message("Inflige 10 points de dégats.",BLACK,(486+x_off_set,456+y_off_set),font2)

					message("(Cliquez dessus pour l'utiliser.)",GREY,(500+x_off_set,480+y_off_set),font_obj_num)

				elif bandage_details_on:
					screen.blit(bandage_for_details,(375+x_off_set,414+y_off_set))
					message("Un rouleau de bandage.",BLACK,(486+x_off_set,424+y_off_set),font2)
					message("Redonne 30 points de vie",BLACK,(486+x_off_set,440+y_off_set),font2)
					message("en cas d'urgence seulement.",BLACK,(486+x_off_set,456+y_off_set),font2)
					message("(Cliquez dessus pour l'utiliser.)",GREY,(500+x_off_set,480+y_off_set),font_obj_num)

				elif key_details_on:
					screen.blit(key_for_details,(384+x_off_set,414+y_off_set))
					message("Une vieille clé rouillée.Quelle",BLACK,(486+x_off_set,424+y_off_set),font2)
					message("porte pourrait-elle bien",BLACK,(486+x_off_set,440+y_off_set),font2)
					message("ouvrir ?",BLACK,(486+x_off_set,456+y_off_set),font2)
					message("(Cliquez dessus pour l'utiliser.)",GREY,(500+x_off_set,480+y_off_set),font_obj_num)

				elif banana_details_on:
					screen.blit(banana_for_details,(384+x_off_set,414+y_off_set))
					message("Bannanes du sud d'afrique.",BLACK,(486+x_off_set,424+y_off_set),font2)
					message("Redonne 10 points de vie.",BLACK,(486+x_off_set,440+y_off_set),font2)
					message("(Cliquez dessus pour l'utiliser.)",GREY,(500+x_off_set,480+y_off_set),font_obj_num)

			if full_energy and timer_energy_1 < 30 and apple_used and (not blocked or timer_energy_1!=0) :
				message("J'ai déjà toute mon energie.",WHITE,(420,8),font2)
				timer_energy_1+=1


			else:
				apple_used = False
				timer_energy_1 = 0
				

			if full_energy and timer_energy_2 < 30 and banana_used and (not blocked or timer_energy_2!=0):
				message("Je devrai le garder pour plus tard.",WHITE,(420,8),font2)
				timer_energy_2+=1

			
			else:
				banana_used = False
				timer_energy_2 = 0

			if  timer_energy_3 < 30 and key_used and (not blocked or timer_energy_3!=0):
				message("Menottes ouvertes avec succès.",WHITE,(420,8),font2)
				timer_energy_3+=1


			else:
				key_used = False
				timer_energy_3 = 0

			if full_energy and timer_energy_4 < 30 and bandage_used and (not blocked or timer_energy_4!=0):
				message("Je n'ai aucune blessure grave.",WHITE,(420,8),font2)
				timer_energy_4+=1

			
				"""apple_used = False
				key_used = False
				banana_used = False
				knife_used = False"""
				
				timer_energy_4+=1
			else:

				bandage_used = False
				timer_energy_4 = 0

			if  timer_energy_5< 30 and  knife_used and (not blocked or timer_energy_5!=0):
				message("Je devrai l'utiliser au bon moment.",WHITE,(420,8),font2)
				timer_energy_5+=1
			else:
				knife_used = False
				timer_energy_5 = 0


			if timer < 40:
				message(logs,logs_color,(400,27),font2)

				timer += 1
			else:
				logs = ""


		
		if quests_clicked :
			screen.blit(quests_open,(300,100))
			message("Journal de quêtes",RED,(485,138),font_text_small)
			pygame.draw.line(screen,RED,[485,160],[630,160],1)
			pygame.draw.rect(screen,RED,[672,127,10,10])
			if not cross_selected1:
				message("x",BLACK,(674,121),font2)
			else:					
				message("x",WHITE,(674,121),font2)
			if page_quests == 0:
				
				if not q1:
					message("- Trouver la clé des menottes.",BLACK,(470,180),font_text_small1)
				else:
					message("- Trouver la clé des menottes.",GREY,(470,180),font_text_small1)
				if not q2:
					message("- Utiliser la clé pour vous libérer.",BLACK,(470,190),font_text_small1)
				else:
					message("- Utiliser la clé pour vous libérer.",GREY,(470,190),font_text_small1)

				if not q3:
					message("- Trouver du bandage.",BLACK,(470,200),font_text_small1)
				else:
					message("- Trouver du bandage.",GREY,(470,200),font_text_small1)

				if not q4:
					message("- Utiliser le bandage pour ",BLACK,(470,210),font_text_small1)
					message("  couvrir tes blesssures.",BLACK,(470,220),font_text_small1)
				else:
					message("- Utiliser le bandage pour ",GREY,(470,210),font_text_small1)
					message("  couvrir tes blesssures.",GREY,(470,220),font_text_small1)

				if not q5:
					message("- Trouver de quoi manger.",BLACK,(470,230),font_text_small1)
				else:
					message("- Trouver de quoi manger.",GREY,(470,230),font_text_small1)

				if not q6:
					message("- Trouver une arme aiguisée.",BLACK,(470,240),font_text_small1)
				else:
					message("- Trouver une arme aiguisée.",GREY,(470,240),font_text_small1)

				if q1*q2*q3*q4*q5*q6:
					if not arrow_right_small1_glow_state:
						screen.blit(arrow_right_small1,(615,300))
					else:
						screen.blit(arrow_right_small1_glow,(615,300))
					show_arrow_left = True
			if page_quests == 1:
				message("-RUN- ",RED,(470,180),font_title_chapter)






		screen.blit(cursor,mouse_position)

		pygame.display.update()
		clock.tick(FPS)













































start_menu()
