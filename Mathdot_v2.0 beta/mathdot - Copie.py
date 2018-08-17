
#Import all needed modules
import pygame , sys
from math import *
from math import log as ln

#Initiliaze pygame
pygame.init()

#Keep track of time
clock = pygame.time.Clock()
FPS = 30

#Define Some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0,255 ,0)
BLUE = (0, 0, 255)
GREY = (60,60,60)
ORANGE = (255,128,0)

#Load images
##TITAN LOL
titan_hand = pygame.image.load('titan_hand.png')
titan_head = pygame.image.load('titan_head.png')

yukina = pygame.image.load('yukina.png')
speech_bubble = pygame.image.load('speech-bubbles-hi.png')
blackwheel = pygame.image.load('blackwheel.png')
## LEVI CLEANING WTF
levi_clean0 =  pygame.image.load('levi_clean0.png')
levi_clean1 =  pygame.image.load('levi_clean1.png')
levi_clean2 =  pygame.image.load('levi_clean2.png')
levi_clean3 =  pygame.image.load('levi_clean3.png')
levi_clean4 =  pygame.image.load('levi_clean4.png')
levi_clean5 =  pygame.image.load('levi_clean5.png')
levi_clean6 =  pygame.image.load('levi_clean6.png')
levi_clean7 =  pygame.image.load('levi_clean7.png')
animation_lst = [levi_clean0,levi_clean1,levi_clean2,levi_clean3,levi_clean4,levi_clean5,levi_clean6,levi_clean7]
π = pi
##Load reference background image
reference_background = pygame.image.load('reference_background.png')
reference_background_width = 600
reference_background_height = 600
reference_background_x = 412
reference_background_y = 12
reference_echelle = 60
reference_background_border_width = 5
offset_regulation = 12
reg_y = 0
reg_x = 0

#AXIS POSITIONNING ( AU CENTRE PAR DEFAUT )
k_x = 1  
k_y = 1
k_center = (reference_background_height//reference_echelle)//2
##load inputpad background image
inputpad_background = pygame.image.load('inputpad_background.png')
inputpad_background_width = 400
inputpad_background_height = 600
inputpad_background_x = 6
inputpad_background_y = 12
intputpad_background_border_width = 10
##load title panel image
title_panel = pygame.image.load('title_panel.png')
title_panel_width = 300
title_panel_height = 100
title_panel_x = inputpad_background_x +50
title_panel_y = inputpad_background_y + 64

##Load function panel image
function_panel = pygame.image.load('function_panel.png')
scroll = pygame.image.load('blue_sliderDown.png')
function_panel_width = 250
function_panel_height = 30
dist_function_panel = 5
##Functions pannel caracterities
pannel_f_x = title_panel_x
pannel_f_y = title_panel_height+title_panel_y+15
pannel_g_x = title_panel_x
pannel_g_y = pannel_f_y + function_panel_height+dist_function_panel
pannel_h_x = title_panel_x
pannel_h_y = pannel_g_y + function_panel_height+dist_function_panel
function_panel_dict = { "r(x)=":((pannel_f_x,pannel_f_y ),(pannel_f_x-20,pannel_f_y+function_panel_height/2),RED),
                        "g(x)=": ((pannel_g_x,pannel_g_y),(pannel_g_x-20,pannel_g_y+function_panel_height/2),GREEN),
                        "h(x)=":((pannel_h_x,pannel_h_y),(pannel_h_x-20,pannel_h_y+function_panel_height/2),BLUE)}
                                


##Load buttons
button_img = pygame.image.load('blue_button01.png')
button_clean = pygame.image.load('clean_button.png')
button_size = 30
button_dist = 5 
button_x = 320
execute_logo_blue = pygame.image.load('execute_logo_blue.png')
execute_logo_red = pygame.image.load('execute_logo_red.png')
execute_logo_green = pygame.image.load('execute_logo_green.png')
clear_logo = pygame.image.load('clear_logo.png')
button_top = {"button_1_f(x)": (( button_x ,pannel_f_y),(button_x + 2 , pannel_f_y +2),execute_logo_red),
              
              "button_1_g(x)": (( button_x ,pannel_g_y),(button_x + 2 , pannel_g_y +2),execute_logo_green),
              
              "button_1_h(x)": (( button_x ,pannel_h_y),(button_x + 2 , pannel_h_y +2),execute_logo_blue),
              "button_clean": (( button_x + button_dist + button_size ,pannel_f_y),(button_x +button_dist + button_size + 5 , pannel_f_y +2 + 40),clear_logo)}


color_text = BLACK
##check boxes
box_noncheck = pygame.image.load('box_nocheck.png')
box_check = pygame.image.load('box_check.png')


box1_current_status = box_check
box2_current_status = box_check
box3_current_status = box_check
box4_current_status = box_check
box5_current_status = box_check
box6_current_status = box_check
box7_current_status = box_check
box8_current_status = box_check
box9_current_status = box_check


box_dist = 5
box_size = 20
box_text_space = 3

box1_x = pannel_f_x
box1_y = pannel_h_y+dist_function_panel+function_panel_height

box2_x = pannel_f_x
box2_y = box1_y + box_dist + box_size

box3_x = pannel_f_x
box3_y = box2_y + box_dist + box_size

box4_x = pannel_f_x + function_panel_width / 3
box4_y = box1_y

box5_x = box4_x
box5_y = box2_y

box6_x = box4_x
box6_y = box3_y

box7_x = box4_x + function_panel_width / 2
box7_y = box4_y

box8_x = box7_x
box8_y = box5_y

box9_x = box7_x
box9_y = box6_y


box_to_check = {"box1":((box1_x,box1_y),box1_current_status,"Grille",(box1_x + box_size + box_text_space , box1_y + box_size/4)),
                "box2":((box2_x,box2_y),box2_current_status,"x axis",(box2_x + box_size + box_text_space , box2_y + box_size/4)),
                "box3":((box3_x,box3_y),box3_current_status,"y axis", ( box3_x + box_size + box_text_space , box3_y + box_size/4)),
                "box4":((box4_x,box4_y),box4_current_status,"Courbe de r", ( box4_x + box_size + box_text_space , box4_y + box_size/4)),
                "box5":((box5_x,box5_y),box5_current_status,"Courbe de g", ( box5_x + box_size + box_text_space, box5_y + box_size/4)),
                "box6":((box6_x,box6_y),box6_current_status,"Courbe de h",( box6_x +box_size + box_text_space,box6_y + box_size/4)),
                "box7":((box7_x,box7_y),box7_current_status,"x Graduation",(box7_x+box_size + box_text_space,box7_y +  box_size/4)),
                "box8":((box8_x,box8_y),box8_current_status,"y Graduation",(box8_x+box_size + box_text_space,box8_y + box_size/4))
                
                }


##FUNCTION KEYBOARD DISPLAY
KB_button_img = pygame.image.load("blue_button_fct_pad.png")
KB_button_width = 40
KB_button_height = 30
KB_button_distance = 5

KB_button1_x = offset_regulation + intputpad_background_border_width
KB_button1_y = box3_y + KB_button_distance +box_size+20

KB_button2_x = KB_button1_x + KB_button_width + KB_button_distance
KB_button2_y = KB_button1_y

KB_button3_x = KB_button2_x + KB_button_width + KB_button_distance
KB_button3_y = KB_button2_y

KB_button4_x = KB_button3_x + KB_button_width + KB_button_distance
KB_button4_y = KB_button3_y

KB_button5_x = KB_button4_x + + KB_button_width + KB_button_distance
KB_button5_y = KB_button4_y

KB_button6_x = KB_button1_x
KB_button6_y = KB_button1_y + KB_button_height + KB_button_distance

KB_button7_x = KB_button2_x
KB_button7_y = KB_button6_y

KB_button8_x = KB_button3_x
KB_button8_y = KB_button6_y

KB_button9_x = KB_button4_x
KB_button9_y = KB_button6_y

KB_button10_x = KB_button5_x
KB_button10_y = KB_button6_y

KB_button11_x = KB_button6_x
KB_button11_y = KB_button10_y + KB_button_height + KB_button_distance

KB_button12_x =KB_button7_x
KB_button12_y =KB_button11_y

KB_button13_x =KB_button8_x
KB_button13_y =KB_button11_y

KB_button14_x =KB_button9_x
KB_button14_y = KB_button11_y

KB_button15_x =KB_button10_x
KB_button15_y = KB_button11_y

KB_button16_x = KB_button11_x
KB_button16_y = KB_button15_y + KB_button_height + KB_button_distance

KB_button17_x =KB_button12_x
KB_button17_y = KB_button16_y

KB_button18_x =KB_button13_x
KB_button18_y = KB_button16_y

KB_button19_x =KB_button14_x
KB_button19_y = KB_button16_y

KB_button20_x =KB_button15_x
KB_button20_y = KB_button16_y



KB_button = { "KB_button1":((KB_button1_x,KB_button1_y),"cos",(KB_button1_x+KB_button_width/2,KB_button1_y+KB_button_height/2)),
              "KB_button2":((KB_button2_x,KB_button2_y),"sin",(KB_button2_x+KB_button_width/2,KB_button2_y+KB_button_height/2)),
              "KB_button3":((KB_button3_x,KB_button3_y),"tan",(KB_button3_x+KB_button_width/2,KB_button3_y+KB_button_height/2)),
              "KB_button4":((KB_button4_x,KB_button4_y),"abs",(KB_button4_x+KB_button_width/2,KB_button4_y+KB_button_height/2)),
              "KB_button5":((KB_button5_x,KB_button5_y),"E",(KB_button5_x+KB_button_width/2,KB_button5_y+KB_button_height/2)),

              "KB_button6":((KB_button6_x,KB_button6_y),"acos",(KB_button6_x+KB_button_width/2,KB_button6_y+KB_button_height/2)),
              "KB_button7":((KB_button7_x,KB_button7_y),"asin",(KB_button7_x+KB_button_width/2,KB_button7_y+KB_button_height/2)),
              "KB_button8":((KB_button8_x,KB_button8_y),"atan",(KB_button8_x+KB_button_width/2,KB_button8_y+KB_button_height/2)),
              "KB_button9":((KB_button9_x,KB_button9_y),"sqrt",(KB_button9_x+KB_button_width/2,KB_button9_y+KB_button_height/2)),
              "KB_button10":((KB_button10_x,KB_button10_y),"π",(KB_button10_x+KB_button_width/2,KB_button10_y+KB_button_height/2)),

              "KB_button11":((KB_button11_x,KB_button11_y),"cosh",(KB_button11_x+KB_button_width/2,KB_button11_y+KB_button_height/2)),
              "KB_button12":((KB_button12_x,KB_button12_y),"sinh",(KB_button12_x+KB_button_width/2,KB_button12_y+KB_button_height/2)),
              "KB_button13":((KB_button13_x,KB_button13_y),"tanh",(KB_button13_x+KB_button_width/2,KB_button13_y+KB_button_height/2)),
              "KB_button14":((KB_button14_x,KB_button14_y),"**",(KB_button14_x+KB_button_width/2,KB_button14_y+KB_button_height/2)),
              "KB_button15":((KB_button15_x,KB_button15_y),"puis(x,",(KB_button15_x+KB_button_width/2,KB_button15_y+KB_button_height/2)),

              "KB_button16":((KB_button16_x,KB_button16_y),"acosh",(KB_button16_x+KB_button_width/2,KB_button16_y+KB_button_height/2)),
              "KB_button17":((KB_button17_x,KB_button17_y),"asinh",(KB_button17_x+KB_button_width/2,KB_button17_y+KB_button_height/2)),
              "KB_button18":((KB_button18_x,KB_button18_y),"atanh",(KB_button18_x+KB_button_width/2,KB_button18_y+KB_button_height/2)),
              "KB_button19":((KB_button19_x,KB_button19_y),"exp",(KB_button19_x+KB_button_width/2,KB_button19_y+KB_button_height/2)),
              "KB_button20":((KB_button20_x,KB_button20_y),"ln",(KB_button20_x+KB_button_width/2,KB_button20_y+KB_button_height/2))

                
              
              }

##NUM PAD BUTTONS

NP_button_img = pygame.image.load('button_num_pad.png')
NP_button_width = 25
NP_button_height = 30
KB_NP_distance = 8
NP_button_distance = 3

NP_button1_x = KB_button5_x + KB_button_width + KB_NP_distance   
NP_button1_y = KB_button1_y

NP_button2_x = NP_button1_x + NP_button_width + NP_button_distance
NP_button2_y = KB_button1_y

NP_button3_x = NP_button2_x + NP_button_width + NP_button_distance
NP_button3_y = KB_button1_y

NP_button4_x = NP_button3_x + NP_button_width + NP_button_distance
NP_button4_y = KB_button1_y

NP_button5_x = NP_button4_x + NP_button_width + NP_button_distance
NP_button5_y = KB_button1_y

NP_button6_x = NP_button1_x
NP_button6_y = KB_button6_y

NP_button7_x = NP_button2_x
NP_button7_y = KB_button6_y

NP_button8_x = NP_button3_x
NP_button8_y = KB_button6_y

NP_button9_x = NP_button4_x
NP_button9_y = KB_button6_y

NP_button10_x = NP_button5_x
NP_button10_y = KB_button6_y

NP_button11_x = NP_button1_x
NP_button11_y = KB_button11_y

NP_button12_x = NP_button2_x
NP_button12_y = KB_button11_y

NP_button13_x = NP_button3_x
NP_button13_y = KB_button11_y

NP_button14_x = NP_button4_x
NP_button14_y = KB_button11_y

NP_button15_x = NP_button5_x
NP_button15_y = KB_button11_y

NP_button16_x = NP_button1_x
NP_button16_y = KB_button16_y

NP_button17_x = NP_button2_x
NP_button17_y = KB_button16_y

NP_button18_x = NP_button3_x
NP_button18_y = KB_button16_y

NP_button19_x = NP_button4_x
NP_button19_y = KB_button16_y 

NP_button20_x = NP_button5_x
NP_button20_y = KB_button16_y 




NP_button = {"NP_button1": ((NP_button1_x,NP_button1_y),"7",(NP_button1_x+NP_button_width/2,NP_button1_y+NP_button_height/2)),
             "NP_button2": ((NP_button2_x,NP_button2_y),"8",(NP_button2_x+NP_button_width/2,NP_button2_y+NP_button_height/2)),
             "NP_button3": ((NP_button3_x,NP_button3_y),"9",(NP_button3_x+NP_button_width/2,NP_button3_y+NP_button_height/2)),
             "NP_button4": ((NP_button4_x,NP_button4_y),"CE",(NP_button4_x+NP_button_width/2,NP_button4_y+NP_button_height/2)),
             "NP_button5": ((NP_button5_x,NP_button5_y),"C",(NP_button5_x+NP_button_width/2,NP_button5_y+NP_button_height/2)),

             "NP_button6": ((NP_button6_x,NP_button6_y),"4",(NP_button6_x+NP_button_width/2,NP_button6_y+NP_button_height/2)),
             "NP_button7": ((NP_button7_x,NP_button7_y),"5",(NP_button7_x+NP_button_width/2,NP_button7_y+NP_button_height/2)),
             "NP_button8": ((NP_button8_x,NP_button8_y),"6",(NP_button8_x+NP_button_width/2,NP_button8_y+NP_button_height/2)),
             "NP_button9": ((NP_button9_x,NP_button9_y),"+",(NP_button9_x+NP_button_width/2,NP_button9_y+NP_button_height/2)),
             "NP_button10": ((NP_button10_x,NP_button10_y),"-",(NP_button10_x+NP_button_width/2,NP_button10_y+NP_button_height/2)),

             "NP_button11": ((NP_button11_x,NP_button11_y),"1",(NP_button11_x+NP_button_width/2,NP_button11_y+NP_button_height/2)),
             "NP_button12": ((NP_button12_x,NP_button12_y),"2",(NP_button12_x+NP_button_width/2,NP_button12_y+NP_button_height/2)),
             "NP_button13": ((NP_button13_x,NP_button13_y),"3",(NP_button13_x+NP_button_width/2,NP_button13_y+NP_button_height/2)),
             "NP_button14": ((NP_button14_x,NP_button14_y),"*",(NP_button14_x+NP_button_width/2,NP_button14_y+NP_button_height/2)),
             "NP_button15": ((NP_button15_x,NP_button15_y),"/",(NP_button15_x+NP_button_width/2,NP_button15_y+NP_button_height/2)),

             "NP_button16": ((NP_button16_x,NP_button16_y),"0",(NP_button16_x+NP_button_width/2,NP_button16_y+NP_button_height/2)),
             "NP_button17": ((NP_button17_x,NP_button17_y),".",(NP_button17_x+NP_button_width/2,NP_button17_y+NP_button_height/2)),
             "NP_button18": ((NP_button18_x,NP_button18_y),"x",(NP_button18_x+NP_button_width/2,NP_button18_y+NP_button_height/2)),
             "NP_button19": ((NP_button19_x,NP_button19_y),"(",(NP_button19_x+NP_button_width/2,NP_button19_y+NP_button_height/2)),
             "NP_button20": ((NP_button20_x,NP_button20_y),")",(NP_button20_x+NP_button_width/2,NP_button20_y+NP_button_height/2)),

             
             }




PART1_LINE_COORD_y = {
    "line1_y": pannel_f_y ,
    "line2_y": pannel_f_y + function_panel_height ,
    "line3_y": pannel_g_y ,
    "line4_y": pannel_g_y + function_panel_height,
    "line5_y": pannel_h_y,
    "line6_y": pannel_h_y + function_panel_height ,
    "line7_y": box1_y ,
    "line8_y": box1_y + box_size , 
    "line9_y": box2_y,
    "line10_y": box2_y + box_size , 
    "line11_y": box3_y,
    "line12_y": box3_y + box_size , 
    }

PART1_LINE_COORD_x = {
    "line1_x": pannel_f_x,
    "line2_x": box1_x + box_size ,
    "line3_x": box4_x ,
    "line4_x": box4_x + box_size,
    "line5_x": box7_x ,
    "line6_x": box7_x + box_size ,
    "line7_x": pannel_f_x + function_panel_width ,
    "line8_x": button_x,
    "line9_x": button_x + button_size,
    "line10_x": button_x + button_dist + button_size,
    "line11_x": button_x + button_dist + 2*button_size ,
    
    }

PART2_LINE_COORD_y = {
    "line1_y": KB_button1_y ,
    "line2_y": KB_button1_y + KB_button_height ,
    "line3_y": KB_button6_y,
    "line4_y": KB_button6_y + KB_button_height,
    "line5_y": KB_button11_y,
    "line6_y": KB_button11_y + KB_button_height,
    "line7_y": KB_button16_y,
    "line8_y": KB_button16_y + KB_button_height,
    }

PART2_LINE_COORD_x = {
    "line1_x": KB_button1_x,
    "line2_x": KB_button1_x + KB_button_width ,
    "line3_x":KB_button2_x,
    "line4_x":KB_button2_x + KB_button_width ,
    "line5_x":KB_button3_x,
    "line6_x":KB_button3_x + KB_button_width ,
    "line7_x":KB_button4_x,
    "line8_x":KB_button4_x + KB_button_width ,
    "line9_x":KB_button5_x,
    "line10_x":KB_button5_x + KB_button_width ,
    "line11_x":NP_button1_x,
    "line12_x":NP_button1_x + NP_button_width,
    "line13_x":NP_button2_x,
    "line14_x":NP_button2_x + NP_button_width,
    "line15_x":NP_button3_x,
    "line16_x":NP_button3_x + NP_button_width,
    "line17_x":NP_button4_x,
    "line18_x":NP_button4_x + NP_button_width,
    "line19_x":NP_button5_x,
    "line20_x":NP_button5_x + NP_button_width,
    
    }


SCROLLERS = {"fx_scroller":(pannel_f_x + function_panel_width-20,pannel_f_y),
             "gx_scroller":(pannel_f_x + function_panel_width-20,pannel_g_y),
             "hx_scroller":(pannel_f_x + function_panel_width-20,pannel_h_y),
             }
             












    
    



                    

#Main window :
    ##Screen Caracteristics
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 624
SCREEN_RESOLUTION = [SCREEN_WIDTH,SCREEN_HEIGHT]
SCREEN_TITLE = "Mathdot v2.0 beta"


    ##Create a screen
SCREEN = pygame.display.set_mode(SCREEN_RESOLUTION)
pygame.display.set_caption(SCREEN_TITLE)



#Functions:
    ##Display text from center
def text_display_center(text,coord,size=11,color=BLACK,police="freesansbold.ttf"):
    myfont = pygame.font.Font(police,size)
    text = myfont.render(text,True,color)
    textRect = text.get_rect()
    textRect.center = coord
    SCREEN.blit(text,textRect)
    ##Display text from left top
def text_display(text,coord,size=11,color=BLACK,police="freesansbold.ttf"):
    myfont = pygame.font.Font(police,size)
    text = myfont.render(text,True,color)

    SCREEN.blit(text,coord)   

    ##Draw the reference :
def draw_reference(reference_echelle,k_x=1,k_y=1,reg_y=0,reg_x=0,grille=True,x_axis_show=True,y_axis_show=True,x_graduation = True , y_graduation = True ):
    reference_echelle_fixe = reference_echelle
    lenght = 2
    discontinue = 2
    x_axis = 10
    y_axis = 10
    i_y = (reference_background_width//reference_echelle)//2 -1+reg_y
    i_x = (reference_background_width//reference_echelle)//2 -1+reg_x
    
    while reference_echelle < reference_background_width-reference_background_border_width:
        start_pos = [offset_regulation+inputpad_background_width+reference_echelle,reference_background_border_width+offset_regulation]
        end_pos = [offset_regulation+inputpad_background_width+reference_echelle,reference_background_height-2*reference_background_border_width+offset_regulation]

        while start_pos[1] + lenght < reference_background_height-reference_background_border_width+offset_regulation/2:           
            if grille:
                pygame.draw.line(SCREEN,GREY,start_pos,[end_pos[0],start_pos[1]+lenght])
            if k_x == k_center :
                if x_axis_show:
                    pygame.draw.line(SCREEN,BLACK,start_pos,end_pos,2)
                x_axis = start_pos[0]
                
            start_pos[1] += lenght + discontinue
        
        reference_echelle += reference_echelle_fixe
        k_x+= 1
        if grille:
            pygame.draw.line(SCREEN,GREY,start_pos,[end_pos[0],reference_background_height-2*reference_background_border_width+offset_regulation])


    reference_echelle =  reference_echelle_fixe
    while reference_echelle < reference_background_width-reference_background_border_width and y_graduation:
        if i_y !=0:
           text_display(str(i_y),(x_axis-12, +reference_echelle),11,BLACK,"freesansbold.ttf")
        i_y-= 1
        reference_echelle+=  reference_echelle_fixe          

        
        
    reference_echelle =  reference_echelle_fixe
    
    while reference_echelle < reference_background_height-reference_background_border_width:
        start_pos = [inputpad_background_width+offset_regulation+reference_background_border_width,reference_background_border_width+offset_regulation/2+reference_echelle]
        end_pos = [reference_background_width+offset_regulation+inputpad_background_width-reference_background_border_width,reference_background_border_width+offset_regulation/2+reference_echelle] 
        while start_pos[0] + lenght < inputpad_background_width+offset_regulation+reference_background_width - reference_background_border_width:            
            if grille :
                pygame.draw.line(SCREEN,GREY,start_pos,[start_pos[0]+lenght,end_pos[1]])
            if k_y == k_center :
                if y_axis_show:
                    pygame.draw.line(SCREEN,BLACK,start_pos,end_pos,2)
                y_axis = start_pos[1]
            start_pos[0] += lenght + discontinue 
        reference_echelle += reference_echelle_fixe
        k_y+= 1
        if grille:
            pygame.draw.line(SCREEN,GREY,start_pos,[inputpad_background_width+reference_background_width+offset_regulation - reference_background_border_width,end_pos[1]])


    reference_echelle =  reference_echelle_fixe
    while reference_echelle < reference_background_width-reference_background_border_width and x_graduation:
        text_display(str(-i_x),(reference_echelle+inputpad_background_width+reference_background_border_width/2, y_axis+5),11,BLACK,"freesansbold.ttf")
        i_x-= 1
        reference_echelle+=  reference_echelle_fixe  

    return x_axis,y_axis

    ##Image calculation function:
def E(x):
    if x < 0:
        return int(x)-1
    else:
        return int(x)

def puis(x,a):
    if x > 0:
        return pow(x,a)
    else:
        return pow(-x,a)
   
        
def f(x,string):
    try:   
        img = eval(string)
        return img 
    except SyntaxError:
        img = -200
        
        return img

    except   NameError:
        img = -200
        
        return img
    
        
    except:
        img = -100
        return img

def r(x,string):
    try:
        img = eval(string)
        return img
    except SyntaxError:
        img = -200  
        return img
    except  :
        img = -200        
        return img

def img_lst_polaire(string,pas = 0.001 , start_x = 0 , end_x = 6.29 ):
    x = start_x
    lst = []
    while x < end_x :
        coord = ( r(x,string)*cos(x) , r(x,string)*sin(x) )
        lst.append(coord)
        x += pas
    return lst

def img_lst(string , pas = 0.001,start_x = -14,end_x = 14):
    x = start_x
    lst = []
    while x < end_x:
        coord = ( x,f(x,string))
        lst.append(coord)
        x+= pas
    return lst

def img_lst_in_reference(reference_echelle,img_lst):
    lst = []
    try:
        for coord in img_lst:
            coord = (coord[0]*reference_echelle,coord[1]*(-reference_echelle))
            lst.append(coord)
        return lst

    except:
        
        return []
def draw_img_group(lst,x_axis,y_axis,courbef_show=True,color=BLACK):
    if courbef_show:
        for coord in lst:
            if reference_background_y + reference_background_border_width <int(coord[1]+y_axis)< reference_background_y+reference_background_height-offset_regulation/2-reference_background_border_width  and reference_background_x + reference_background_border_width-1 <int(coord[0]+x_axis)< reference_background_x + reference_background_width - reference_background_border_width:
                coord = (int(coord[0]+x_axis+2),int(coord[1]+y_axis))
                pygame.draw.circle(SCREEN ,color,(int_overflow(coord[0]),int_overflow(coord[1])),1,1)

def int_overflow(val):
  if not -sys.maxsize-1 <= val <= sys.maxsize:
    val = (val + (sys.maxsize + 1)) % (2 * (sys.maxsize + 1)) - sys.maxsize - 1
  return val
    





grille= True

x_axis_show = True
y_axis_show = True

courbef_show = True
courbeg_show = True
courbeh_show = True


x_graduation = True
y_graduation = True

cleaning_animation = False

f_getting_typed = False
g_getting_typed = False
h_getting_typed = False

MESSAGE = ""

lst_fx = []
lst_gx = []
lst_hx = []
i0 = 0
i1= 0
i2 = 0 # To minimize processing


lst_f_scroller = []
lst_h_scroller = []
lst_g_scroller = []

lst = []
lst1 = []
lst2=[]
he_pressed_f = False


f_scroller = False
g_scroller = False
h_scroller = False

execute_f = False
execute_g = False
execute_h = False

show_f_inclean = False
n = 0

start_posf = -14
end_posf = 14

start_posg = -14
end_posg = 14

start_posh = -14
end_posh = 14

#Main software loop
done = False
while not done :

        
    
    box_to_check = {"box1":((box1_x,box1_y),box1_current_status,"Grille",(box1_x + box_size + box_text_space , box1_y + box_size/4)),
                "box2":((box2_x,box2_y),box2_current_status,"x axis",(box2_x + box_size + box_text_space , box2_y + box_size/4)),
                "box3":((box3_x,box3_y),box3_current_status,"y axis", ( box3_x + box_size + box_text_space , box3_y + box_size/4)),
                "box4":((box4_x,box4_y),box4_current_status,"Courbe de f", ( box4_x + box_size + box_text_space , box4_y + box_size/4)),
                "box5":((box5_x,box5_y),box5_current_status,"Courbe de g", ( box5_x + box_size + box_text_space, box5_y + box_size/4)),
                "box6":((box6_x,box6_y),box6_current_status,"Courbe de h",( box6_x +box_size + box_text_space,box6_y + box_size/4)),
                "box7":((box7_x,box7_y),box7_current_status,"x Graduation",(box7_x+box_size + box_text_space,box7_y +  box_size/4)),
                "box8":((box8_x,box8_y),box8_current_status,"y Graduation",(box8_x+box_size + box_text_space,box8_y + box_size/4))
                
                }



    
    k_center = (reference_background_height//reference_echelle)//2
    #Gets all the event from the user ( keyboard press , mouse click or move...)
    for event in pygame.event.get():
        #Close the window if the user click on the red cross
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                k_x -= 1
                reg_x += 1
            if event.key == pygame.K_LEFT :
                k_x += 1
                reg_x -= 1
            if event.key == pygame.K_DOWN:
                k_y -= 1
                reg_y+=1
            if event.key == pygame.K_UP:
                k_y += 1
                reg_y-=1
            if event.type == pygame.KEYDOWN and f_getting_typed:   
                 if event.key == pygame.K_q:
                      lst_fx.append("a")

                 if event.key == pygame.K_z:
                      lst_fx.append("w")

                 if event.key == pygame.K_e:
                      lst_fx.append("e")

                 if event.key == pygame.K_r:
                     lst_fx.append("r")

                 if event.key == pygame.K_t:
                     lst_fx.append("t")

                 if event.key == pygame.K_y:
                     lst_fx.append("y")

                 if event.key == pygame.K_u:
                     lst_fx.append("u")

                 if event.key == pygame.K_i:
                     lst_fx.append("i")

                 if event.key == pygame.K_o:
                     lst_fx.append("o")

                 if event.key == pygame.K_p:
                     lst_fx.append("p")
                 if event.key == pygame.K_a:
                     lst_fx.append("q")

                 if event.key == pygame.K_s:
                     lst_fx.append("s")

                 if event.key == pygame.K_d:
                     lst_fx.append("d")
                        
                 if event.key == pygame.K_f:
                     lst_fx.append("f")

                 if event.key == pygame.K_g:
                     lst_fx.append("g")

                 if event.key == pygame.K_h:
                     lst_fx.append("h")

                 if event.key == pygame.K_j:
                     lst_fx.append("j")

                 if event.key == pygame.K_k:
                     lst_fx.append("k")

                 if event.key == pygame.K_l:
                     lst_fx.append("l")

                 if event.key == pygame.K_w:
                     lst_fx.append("z")
                
                 if event.key == pygame.K_x:
                     lst_fx.append("x")

                 if event.key == pygame.K_c:
                     lst_fx.append("c")

                 if event.key == pygame.K_b:
                     lst_fx.append("b")

                 if event.key == pygame.K_n:
                     lst_fx.append("n")

                 if event.key == pygame.K_v:
                     lst_fx.append("v")

                 if event.key == pygame.K_1:
                    lst_fx.append("1")

                 if event.key == pygame.K_2:
                    lst_fx.append("2")

                 if event.key == pygame.K_3:
                    lst_fx.append("3")

                 if event.key == pygame.K_4:
                    lst_fx.append("4")

                 if event.key == pygame.K_5:
                    lst_fx.append("5")

                 if event.key == pygame.K_6:
                    lst_fx.append("6")

                 if event.key == pygame.K_7:
                    lst_fx.append("7")

                 if event.key == pygame.K_8:
                    lst_fx.append("8")

                 if event.key == pygame.K_9:
                    lst_fx.append("9")

                 if event.key == pygame.K_0:
                    lst_fx.append("0")

                 if event.key == pygame.K_PLUS:
                    lst_fx.append("-")




                    
                 if event.key == pygame.K_SEMICOLON :
                     lst_fx.append("m")

            if event.key == pygame.K_BACKSPACE and len( lst_fx)>0:                
                del  lst_fx[-1]
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 4 and reference_echelle < 100:
                reference_echelle += 10
            if event.button == 5 and reference_echelle > 40:
                reference_echelle -= 10
                

    #MAIN BUTTONS LOGIC
            if  PART1_LINE_COORD_y["line1_y"]< mouse_pos[1] <   PART1_LINE_COORD_y["line2_y"]:
                if PART1_LINE_COORD_x["line1_x"]< mouse_pos[0]< PART1_LINE_COORD_x["line7_x"]  :
                    f_getting_typed = True
                    g_getting_typed = False
                    h_getting_typed = False
                    f_scroller = False
                    g_scroller = False
                    h_scroller = False
                    MESSAGE = "f(x) is getting typed sir !"

                if PART1_LINE_COORD_x["line8_x"]< mouse_pos[0]< PART1_LINE_COORD_x["line9_x"]  :
                    i0 = 0
                    execute_f = True
                               
                    if f(0, string_fx ) == -200:
                        MESSAGE = "Sir , There is a syntax Error in f(x)."
                    else:
                        MESSAGE = "You have executed f(x) sir !"
      
            
            elif  PART1_LINE_COORD_y["line3_y"]< mouse_pos[1] <   PART1_LINE_COORD_y["line4_y"]:
                if PART1_LINE_COORD_x["line1_x"]< mouse_pos[0]< PART1_LINE_COORD_x["line7_x"]  :
                    g_getting_typed = True
                    f_getting_typed = False
                    h_getting_typed = False
                    f_scroller = False
                    g_scroller = False
                    h_scroller = False
                    MESSAGE = "g(x) is getting typed sir !"

                elif PART1_LINE_COORD_x["line8_x"]< mouse_pos[0]< PART1_LINE_COORD_x["line9_x"]  :

                    i1 = 0
                    execute_g = True
                    if f(0, string_gx ) == -200:
                        MESSAGE = "Sir , There is a syntax Error in g(x)."
                    else:
                        MESSAGE = "You have executed g(x) sir !"
           
                    
            elif  PART1_LINE_COORD_y["line5_y"]< mouse_pos[1] <   PART1_LINE_COORD_y["line6_y"]:
                if PART1_LINE_COORD_x["line1_x"]< mouse_pos[0]< PART1_LINE_COORD_x["line7_x"]  :
                    f_getting_typed = False
                    g_getting_typed = False
                    h_getting_typed = True
                    f_scroller = False
                    g_scroller = False
                    h_scroller = False

                    MESSAGE = "h(x) is getting typed sir !"
                

                elif PART1_LINE_COORD_x["line8_x"]< mouse_pos[0]< PART1_LINE_COORD_x["line9_x"]  :
                    i2 = 0
                    execute_h = True
                    if f(0, string_hx ) == -200:
                        MESSAGE = "Sir , There is a syntax Error in h(x)."
                    else:
                        MESSAGE = "You have executed h(x) sir !"


            elif  PART1_LINE_COORD_y["line7_y"]< mouse_pos[1] <   PART1_LINE_COORD_y["line8_y"]:
                if PART1_LINE_COORD_x["line1_x"]< mouse_pos[0]< PART1_LINE_COORD_x["line2_x"]:
                    if box1_current_status == box_check :
                        box1_current_status = box_noncheck
                        grille = False
                        MESSAGE = "Sir , the Grid has been disabled !"
                    else:
                        box1_current_status = box_check
                        grille = True
                        MESSAGE = "Sir , the Grid has been enabled !"
                        

                elif PART1_LINE_COORD_x["line3_x"]< mouse_pos[0]< PART1_LINE_COORD_x["line4_x"]:
                    if box4_current_status == box_check :
                        box4_current_status = box_noncheck
                        courbef_show = False
                        MESSAGE = "Sir , Cf has been disabled !"
                    else:
                        box4_current_status = box_check
                        courbef_show = True
                        MESSAGE = "Sir , Cf has been enabled !"

                elif PART1_LINE_COORD_x["line5_x"]< mouse_pos[0]< PART1_LINE_COORD_x["line6_x"]:
                    if box7_current_status == box_check :
                        box7_current_status = box_noncheck
                        x_graduation = False
                        MESSAGE = "Sir , x graduation has been disabled !"
                    else:
                        box7_current_status = box_check
                        x_graduation = True
                        MESSAGE = "Sir , x graduation has been enabled !"
                        
            elif  PART1_LINE_COORD_y["line9_y"]< mouse_pos[1] <   PART1_LINE_COORD_y["line10_y"]:
                if PART1_LINE_COORD_x["line1_x"]< mouse_pos[0]< PART1_LINE_COORD_x["line2_x"]:
                    if box2_current_status == box_check :
                        box2_current_status = box_noncheck
                        y_axis_show = False
                        MESSAGE = "Sir , y axis has been disabled !"
                        
                    else:
                        box2_current_status = box_check
                        y_axis_show = True
                        MESSAGE = "Sir , x axis has been enabled !"

                elif PART1_LINE_COORD_x["line3_x"]< mouse_pos[0]< PART1_LINE_COORD_x["line4_x"]:
                    if box5_current_status == box_check :
                        box5_current_status = box_noncheck
                        courbeg_show = False
                        MESSAGE = "Sir , Cg has been disabled !"

                    else:
                        box5_current_status = box_check
                        courbeg_show = True
                        MESSAGE = "Sir , Cg has been enabled !"

                elif PART1_LINE_COORD_x["line5_x"]< mouse_pos[0]< PART1_LINE_COORD_x["line6_x"]:
                    if box8_current_status == box_check :
                        box8_current_status = box_noncheck
                        y_graduation = False
                        MESSAGE = "Sir ,y graduation has been disabled !"
                        
                    else:
                        box8_current_status = box_check
                        y_graduation = True
                        MESSAGE = "Sir ,y graduation has been enabled !"
                        
            elif  PART1_LINE_COORD_y["line11_y"]< mouse_pos[1] <   PART1_LINE_COORD_y["line12_y"]:
                if PART1_LINE_COORD_x["line1_x"]< mouse_pos[0]< PART1_LINE_COORD_x["line2_x"]:
                    if box3_current_status == box_check :
                        box3_current_status = box_noncheck
                        x_axis_show = False
                        MESSAGE = "Sir ,x axis has been disabled !"
                        
                    else:
                        box3_current_status = box_check
                        x_axis_show = True
                        MESSAGE = "Sir ,x axis has been enabled !"

                elif PART1_LINE_COORD_x["line3_x"]< mouse_pos[0]< PART1_LINE_COORD_x["line4_x"]:
                    if box6_current_status == box_check :
                        box6_current_status = box_noncheck
                        courbeh_show = False
                        MESSAGE = "Sir ,Ch has been disabled !"
                    else:
                        box6_current_status = box_check
                        courbeh_show = True
                        MESSAGE = "Sir ,Ch has been enabled !"
            

                
            ##BUTTON CONTROL FOR THE KEYPAD
            elif PART2_LINE_COORD_y["line1_y"] < mouse_pos[1] < PART2_LINE_COORD_y["line2_y"]:
                if PART2_LINE_COORD_x["line1_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line2_x"] :
                    
                    if f_getting_typed:
                        execute_f = False 
                        lst_fx.append("cos")
                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("cos")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("cos")


                elif PART2_LINE_COORD_x["line3_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line4_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("sin")
                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("sin")
                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("sin")

                elif PART2_LINE_COORD_x["line5_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line6_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("tan")
                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("tan")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("tan")

                elif PART2_LINE_COORD_x["line7_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line8_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("abs")
                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("abs")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("abs")

                elif PART2_LINE_COORD_x["line9_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line10_x"]:
                   
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("E")
                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("E")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("E")

                elif PART2_LINE_COORD_x["line11_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line12_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("7")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("7")
                        
                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("7")

                    if f_scroller:
                        lst_f_scroller.append("7")

                    if g_scroller:
                        lst_g_scroller.append("7")

                    if h_scroller:
                        lst_h_scroller.append("7")


                elif PART2_LINE_COORD_x["line13_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line14_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("8")
                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("8")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("8")

                    if f_scroller:
                        lst_f_scroller.append("8")

                    if g_scroller:
                        lst_g_scroller.append("8")

                    if h_scroller:
                        lst_h_scroller.append("8")
                        
                elif PART2_LINE_COORD_x["line15_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line16_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("9")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("9")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("9")

                    if f_scroller:
                        lst_f_scroller.append("9")

                    if g_scroller:
                        lst_g_scroller.append("9")

                    if h_scroller:
                        lst_h_scroller.append("9")

                    
                        

                elif PART2_LINE_COORD_x["line17_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line18_x"]:
                    
                    
                    if f_getting_typed:
                        lst = []
                        execute_f = False
                        lst_fx = []

                    
                    elif g_getting_typed:
                        lst1 = []
                        execute_g = False
                        lst_gx = []

                    elif h_getting_typed:
                        lst2 = []
                        execute_h = False
                        lst_hx = []
                        
                        
                elif PART2_LINE_COORD_x["line19_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line20_x"]:
                    
                    if f_getting_typed and len(lst_fx)>0:
                        execute_f = False
                        del lst_fx[-1]
                    elif g_getting_typed and len(lst_gx)>0:
                        execute_g = False
                        del lst_gx[-1]
                    elif h_getting_typed and len(lst_hx)>0:
                        execute_h = False
                        del lst_hx[-1]

                    if f_scroller and len(lst_f_scroller)>0:
                        
                        del lst_f_scroller[-1]
                        
                    if g_scroller and len(lst_g_scroller)>0:
                        
                        del lst_g_scroller[-1]

                    if h_scroller and len(lst_h_scroller)>0:
                        
                        del lst_h_scroller[-1]

                        

            elif PART2_LINE_COORD_y["line3_y"] < mouse_pos[1] < PART2_LINE_COORD_y["line4_y"]:
                if PART2_LINE_COORD_x["line1_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line2_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("acos")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("acos")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("acos")

                elif PART2_LINE_COORD_x["line3_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line4_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("asin")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("asin")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("asin")
                        
                elif PART2_LINE_COORD_x["line5_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line6_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("atan")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("atan")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("atan")

                elif PART2_LINE_COORD_x["line7_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line8_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("sqrt")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("sqrt")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("sqrt")

                elif PART2_LINE_COORD_x["line9_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line10_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("π")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("π")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("π")

                    if f_scroller:
                        lst_f_scroller.append("π")

                    if g_scroller:
                        lst_g_scroller.append("π")

                    if h_scroller:
                        lst_h_scroller.append("π")

                elif PART2_LINE_COORD_x["line11_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line12_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("4")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("4")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("4")

                    if f_scroller:
                        lst_f_scroller.append("4")

                    if g_scroller:
                        lst_g_scroller.append("4")

                    if h_scroller:
                        lst_h_scroller.append("4")

                    

                      

                elif PART2_LINE_COORD_x["line13_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line14_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("5")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("5")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("5")
                    if f_scroller:
                        lst_f_scroller.append("5")

                    if g_scroller:
                        lst_g_scroller.append("5")

                    if h_scroller:
                        lst_h_scroller.append("5")

                    

                elif PART2_LINE_COORD_x["line15_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line16_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("6")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("6")
                        
                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("6")

                    if f_scroller:
                        lst_f_scroller.append("6")

                    if g_scroller:
                        lst_g_scroller.append("6")

                    if h_scroller:
                        lst_h_scroller.append("6")

                    

                elif PART2_LINE_COORD_x["line17_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line18_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("+")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("+")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("+")

                elif PART2_LINE_COORD_x["line19_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line20_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("-")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("-")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("-")

                    elif f_scroller:
                        lst_f_scroller.append("-")

                    elif g_scroller:
                        lst_g_scroller.append("-")

                    elif h_scroller:
                        lst_h_scroller.append("-")


                    

            elif PART2_LINE_COORD_y["line5_y"] < mouse_pos[1] < PART2_LINE_COORD_y["line6_y"]:
                if PART2_LINE_COORD_x["line1_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line2_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("cosh")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("cosh")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("cosh")

                elif PART2_LINE_COORD_x["line3_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line4_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("sinh")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("sinh")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("sinh")
                        
                elif PART2_LINE_COORD_x["line5_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line6_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("tanh")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("tanh")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("tanh")

                    

                elif PART2_LINE_COORD_x["line7_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line8_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("**")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("**")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("**")


                elif PART2_LINE_COORD_x["line9_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line10_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("puis(x,")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("puis(x,")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("puis(x,")


                if PART2_LINE_COORD_x["line11_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line12_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("1")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("1")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("1")

                    elif f_scroller:
                        lst_f_scroller.append("1")

                    elif g_scroller:
                        lst_g_scroller.append("1")

                    elif h_scroller:
                        lst_h_scroller.append("1")


                elif PART2_LINE_COORD_x["line13_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line14_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("2")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("2")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("2")

                    elif f_scroller:
                        lst_f_scroller.append("2")

                    elif g_scroller:
                        lst_g_scroller.append("2")

                    elif h_scroller:
                        lst_h_scroller.append("2")


                elif PART2_LINE_COORD_x["line15_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line16_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("3")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("3")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("3")

                    elif f_scroller:
                        lst_f_scroller.append("3")

                    elif g_scroller:
                        lst_g_scroller.append("3")

                    elif h_scroller:
                        lst_h_scroller.append("3")

                    

                elif PART2_LINE_COORD_x["line17_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line18_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("*")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("*")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("*")

                    elif f_scroller:
                        lst_f_scroller.append("*")

                    elif g_scroller:
                        lst_g_scroller.append("*")

                    elif h_scroller:
                        lst_h_scroller.append("*")
                    

                elif PART2_LINE_COORD_x["line19_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line20_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("/")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("/")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("/")

                    elif f_scroller:
                        lst_f_scroller.append("/")

                    elif g_scroller:
                        lst_g_scroller.append("/")

                    elif h_scroller:
                        lst_h_scroller.append("/")
                        




            elif PART2_LINE_COORD_y["line7_y"] < mouse_pos[1] < PART2_LINE_COORD_y["line8_y"]:
                if PART2_LINE_COORD_x["line1_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line2_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("acosh")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("acosh")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("acosh")


                elif PART2_LINE_COORD_x["line3_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line4_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("asinh")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("asinh")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("asinh")

                        
                elif PART2_LINE_COORD_x["line5_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line6_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("atanh")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("atanh")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("atanh")


                elif PART2_LINE_COORD_x["line7_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line8_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("exp")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("exp")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("exp")


                elif PART2_LINE_COORD_x["line9_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line10_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("ln")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("ln")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("ln")


                elif PART2_LINE_COORD_x["line11_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line12_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("0")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("0")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("0")

                    elif f_scroller:
                        lst_f_scroller.append("0")

                    elif g_scroller:
                        lst_g_scroller.append("0")

                    elif h_scroller:
                        lst_h_scroller.append("0")
                        

                elif PART2_LINE_COORD_x["line13_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line14_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append(".")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append(".")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append(".")


                    elif f_scroller:
                        lst_f_scroller.append(",")

                    elif g_scroller:
                        lst_g_scroller.append(",")

                    elif h_scroller:
                        lst_h_scroller.append(",")
                        
                        
                elif PART2_LINE_COORD_x["line15_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line16_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("x")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("x")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("x")
                

                elif PART2_LINE_COORD_x["line17_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line18_x"]:
                    
                    if f_getting_typed:
                        execute_f = False
                        lst_fx.append("(")

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append("(")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append("(")

                elif PART2_LINE_COORD_x["line19_x"] <  mouse_pos[0] < PART2_LINE_COORD_x["line20_x"]:
                    
                    if f_getting_typed:
                        lst_fx.append(")")
                        execute_f = False

                    elif g_getting_typed:
                        execute_g = False
                        lst_gx.append(")")

                    elif h_getting_typed:
                        execute_h = False
                        lst_hx.append(")")

            
            if PART1_LINE_COORD_y["line1_y"]< mouse_pos[1] <   PART1_LINE_COORD_y["line6_y"]:
                if PART1_LINE_COORD_x["line10_x"]< mouse_pos[0]< PART1_LINE_COORD_x["line11_x"] :
                    cleaning_animation = True
                    execute_f = False
                    execute_g = False
                    execute_h = False
                   
                    lst_fx = []
                    lst_gx = []
                    lst_hx = []

                    MESSAGE = "Levi cleaned your shit successfuly."

            if PART2_LINE_COORD_x["line1_x"] + 270 < mouse_pos[0] < PART2_LINE_COORD_x["line1_x"] + 290:
                
                if PART2_LINE_COORD_y["line8_y"]+50 < mouse_pos[1] < PART2_LINE_COORD_y["line8_y"]+70:
                    n+= 1 
                    


            if PART1_LINE_COORD_y["line1_y"]< mouse_pos[1] <   PART1_LINE_COORD_y["line2_y"]:
                if SCROLLERS["fx_scroller"][0]< mouse_pos[0]< SCROLLERS["fx_scroller"][0]+20 :
                    f_scroller = True
                    f_getting_typed = False
                    execute_f = False

            if PART1_LINE_COORD_y["line3_y"]< mouse_pos[1] <   PART1_LINE_COORD_y["line4_y"]:
                if SCROLLERS["gx_scroller"][0]< mouse_pos[0]< SCROLLERS["gx_scroller"][0]+20 :
                    print("you pressed it g")
                    g_scroller = True
                    g_getting_typed = False
                    execute_g = False

            if PART1_LINE_COORD_y["line5_y"]< mouse_pos[1] <   PART1_LINE_COORD_y["line6_y"]:
                if SCROLLERS["hx_scroller"][0]< mouse_pos[0]< SCROLLERS["hx_scroller"][0]+20 :
                    print("you pressed it h")
                    h_scroller = True
                    h_getting_typed = False
                    execute_h = False
 
                

            
                

            
            
    s =""
    string_fx = str(s.join(lst_fx))
    string_gx = str(s.join(lst_gx))
    string_hx = str(s.join(lst_hx))
    string_fscroller = s.join(lst_f_scroller)
    string_gscroller = s.join(lst_g_scroller)
    string_hscroller = s.join(lst_h_scroller)
    
    splited_fscroller = string_fscroller.split(",")
    splited_gscroller = string_gscroller.split(",")
    splited_hscroller = string_hscroller.split(",")


    
    if  len(lst_f_scroller)>2 and execute_f :
        start_posf  = eval(splited_fscroller[0])
        end_posf = eval(splited_fscroller[1])
    else:
        start_posf = -14
        end_posf = 14
        

    if  len(lst_g_scroller)>2 and execute_g :
        start_posg  = eval(splited_gscroller[0])
        end_posg = eval(splited_gscroller[1])
    else:
        start_posg = -14
        end_posg = 14

    if  len(lst_h_scroller)>2 and execute_h :
        start_posh  = eval(splited_hscroller[0])
        end_posh = eval(splited_hscroller[1])
    else:
        start_posh = -14
        end_posh = 14

        
    if execute_f and i0 == 0:
        lst = img_lst_polaire(string_fx , 0.001 ,start_posf, end_posf)
        i0=1

    if execute_g and i1 == 0:
        lst1 = img_lst(string_gx,0.001,start_posg, end_posg )
        i1=1


    if execute_h and i2 == 0:
        lst2 = img_lst(string_hx,0.001,start_posh, end_posh )
        i2=1

    

    
    #Blit screen background
    SCREEN.fill(WHITE)

    #MAIN DISPLAY CHANGE
    ##------------------



    #Display images loaded


    SCREEN.blit(reference_background,(reference_background_x,reference_background_y))
    i = 0
    k = 0
    while cleaning_animation and k<15:
        SCREEN.blit(reference_background,(reference_background_x,reference_background_y))
        if i > 7:
            i = 0 
        SCREEN.blit(animation_lst[i],(450,30))
        draw_reference(reference_echelle,k_x,k_y,reg_y,reg_x,grille,x_axis_show,y_axis_show,x_graduation,y_graduation)
        
        draw_img_group(img_lst_in_reference(reference_echelle,lst),x_axis,y_axis,courbef_show)
        
        draw_img_group(img_lst_in_reference(reference_echelle,lst1),x_axis,y_axis,courbeg_show)
        
        draw_img_group(img_lst_in_reference(reference_echelle,lst2),x_axis,y_axis,courbeh_show)
        i+= 1
        k+=1
        pygame.display.update([reference_background_x,reference_background_y,reference_background_width,reference_background_height])
        #Set up the speed of the loop
        clock.tick(30)

    if k>=15:
        lst = []
        lst1 = []
        lst2 = []
    cleaning_animation = False 

    
    SCREEN.blit(inputpad_background,(inputpad_background_x,inputpad_background_y))
    SCREEN.blit(title_panel,(title_panel_x,title_panel_y))
    SCREEN.blit(titan_hand,(title_panel_x+title_panel_width*(1/2)-15,69))
    SCREEN.blit(titan_head,(title_panel_x+title_panel_width*(1/2)+5,27))


    

    ##blit function pannels
    for fct in function_panel_dict:
        SCREEN.blit(function_panel,function_panel_dict[fct][0])
        text_display_center(fct,function_panel_dict[fct][1],15,function_panel_dict[fct][2],"freesansbold.ttf")
    ## blit buttons
    for button in button_top:
        SCREEN.blit(button_img,button_top[button][0])
        SCREEN.blit(button_top[button][2],button_top[button][1])
    SCREEN.blit(button_clean,button_top["button_clean"][0])
    SCREEN.blit(button_top["button_clean"][2],button_top["button_clean"][1])
    

    for box in box_to_check:
        SCREEN.blit(box_to_check[box][1],box_to_check[box][0])
        text_display(box_to_check[box][2],box_to_check[box][3],11,BLACK,"freesansbold.ttf")

    for button in KB_button:
        SCREEN.blit(KB_button_img,KB_button[button][0])
        text_display_center(KB_button[button][1],KB_button[button][2],11,WHITE,"freesansbold.ttf")

    for button in NP_button:
        SCREEN.blit(NP_button_img,NP_button[button][0])
        text_display_center(NP_button[button][1],NP_button[button][2],11,WHITE,"freesansbold.ttf")

    for scroller in SCROLLERS:
        SCREEN.blit(scroll,SCROLLERS[scroller])
        
    #Display texts
    text_display_center("MATHDOT",(inputpad_background_x+(inputpad_background_width)/2+5,inputpad_background_y+64+title_panel_height/2),47,BLACK)
    text_display_center("MATHDOT 2.0 beta ", (title_panel_x+title_panel_width-11,title_panel_y+title_panel_height+8),8,GREY)

    text_display("Ce logiciel a été crée dans le cadre du TIPE au CPGE Salmane Al Farissi par Amine Elmouradi en 12/2016 , encadré par les professeurs Baba Abdsalam et Ali Choukri.",(15,SCREEN_HEIGHT-10),8,GREY)

    if f_getting_typed:
        pygame.draw.rect(SCREEN,ORANGE,[pannel_f_x,pannel_f_y,function_panel_width,function_panel_height],1)
    text_display(string_fx,(pannel_f_x + 8 , pannel_f_y +8 ),11,BLACK,"freesansbold.ttf")

    if g_getting_typed:
        pygame.draw.rect(SCREEN,ORANGE,[pannel_g_x,pannel_g_y,function_panel_width,function_panel_height],1)
    text_display(string_gx,(pannel_g_x + 8 , pannel_g_y +8 ),11,BLACK,"freesansbold.ttf")

    if h_getting_typed:
        pygame.draw.rect(SCREEN,ORANGE,[pannel_h_x,pannel_h_y,function_panel_width,function_panel_height],1)
    text_display(string_hx,(pannel_h_x + 8 , pannel_h_y +8 ),11,BLACK,"freesansbold.ttf")
        
    
    #Draw reference
    x_axis,y_axis = draw_reference(reference_echelle,k_x,k_y,reg_y,reg_x,grille,x_axis_show,y_axis_show,x_graduation,y_graduation)    

    #Draw function
    if execute_f:
       
        draw_img_group(img_lst_in_reference(reference_echelle,lst),x_axis,y_axis,courbef_show,RED)

    if execute_g:
        draw_img_group(img_lst_in_reference(reference_echelle,lst1),x_axis,y_axis,courbeg_show,GREEN)

    if execute_h:
        draw_img_group(img_lst_in_reference(reference_echelle,lst2),x_axis,y_axis,courbeh_show,BLUE)

    SCREEN.blit(yukina, (PART2_LINE_COORD_x["line1_x"],PART2_LINE_COORD_y["line8_y"]+5))
    SCREEN.blit(speech_bubble , ( PART2_LINE_COORD_x["line1_x"] + 60 , PART2_LINE_COORD_y["line8_y"]+12))

    if f_scroller:
        pygame.draw.rect(SCREEN,ORANGE,[SCROLLERS["fx_scroller"][0]-60,SCROLLERS["fx_scroller"][1]+5,60,15])
        text_display(string_fscroller,(SCROLLERS["fx_scroller"][0]-52,SCROLLERS["fx_scroller"][1]+7),8,BLACK,"freesansbold.ttf")
        text_display("[                ]",(SCROLLERS["fx_scroller"][0]-58,SCROLLERS["fx_scroller"][1]+7),11,BLACK,"freesansbold.ttf")

    if g_scroller:
        pygame.draw.rect(SCREEN,ORANGE,[SCROLLERS["gx_scroller"][0]-60,SCROLLERS["gx_scroller"][1]+5,60,15])
        text_display(string_gscroller,(SCROLLERS["gx_scroller"][0]-52,SCROLLERS["gx_scroller"][1]+7),8,BLACK,"freesansbold.ttf")
        text_display("[                ]",(SCROLLERS["gx_scroller"][0]-58,SCROLLERS["gx_scroller"][1]+7),11,BLACK,"freesansbold.ttf")

    if h_scroller:
        pygame.draw.rect(SCREEN,ORANGE,[SCROLLERS["hx_scroller"][0]-60,SCROLLERS["hx_scroller"][1]+5,60,15])
        text_display(string_hscroller,(SCROLLERS["hx_scroller"][0]-52,SCROLLERS["hx_scroller"][1]+7),8,BLACK,"freesansbold.ttf")
        text_display("[                ]",(SCROLLERS["hx_scroller"][0]-58,SCROLLERS["hx_scroller"][1]+7),11,BLACK,"freesansbold.ttf")

    
        
    
    if n == 0 :
        text_display("Hello! My name is Yukina , and I'll be ",(PART2_LINE_COORD_x["line1_x"] + 105 , PART2_LINE_COORD_y["line8_y"]+18 ),11,BLACK,"freesansbold.ttf")
        text_display("your assistant in this program. ",(PART2_LINE_COORD_x["line1_x"] + 105 , PART2_LINE_COORD_y["line8_y"]+32 ),11,BLACK,"freesansbold.ttf")
        text_display("Don't worry its easy to use. ",(PART2_LINE_COORD_x["line1_x"] + 105 , PART2_LINE_COORD_y["line8_y"]+46 ),11,BLACK,"freesansbold.ttf")
    if n<= 5:
        text_display("Next>>",(PART2_LINE_COORD_x["line1_x"] + 270 , PART2_LINE_COORD_y["line8_y"]+50 ),8,ORANGE,"freesansbold.ttf")

    if n==1 :
        text_display("This is the zone where you will enter ",(PART2_LINE_COORD_x["line1_x"] + 105 , PART2_LINE_COORD_y["line8_y"]+18 ),11,BLACK,"freesansbold.ttf")
        text_display("the different functions you need. ",(PART2_LINE_COORD_x["line1_x"] + 105 , PART2_LINE_COORD_y["line8_y"]+32 ),11,BLACK,"freesansbold.ttf")
        text_display("be careful about Syntax errors. ",(PART2_LINE_COORD_x["line1_x"] + 105 , PART2_LINE_COORD_y["line8_y"]+46 ),11,BLACK,"freesansbold.ttf")
        pygame.draw.rect(SCREEN,RED,[pannel_f_x-40,pannel_f_y-10 ,function_panel_width+50 , function_panel_height*3+20],2)
        

    if n == 2 :
        
        pygame.draw.rect(SCREEN,RED,[function_panel_width+60,pannel_f_y-5 ,80 , function_panel_height*3+20-3],2)
        SCREEN.blit(blackwheel,(PART2_LINE_COORD_x["line1_x"] + 105 ,PART2_LINE_COORD_y["line8_y"]+15 ))
        SCREEN.blit(clear_logo,(PART2_LINE_COORD_x["line1_x"] + 105 ,PART2_LINE_COORD_y["line8_y"]+40 ))
        text_display("execute the function. ",(PART2_LINE_COORD_x["line1_x"] + 135 , PART2_LINE_COORD_y["line8_y"]+22 ),11,BLACK,"freesansbold.ttf")
        text_display("clear all the functions",(PART2_LINE_COORD_x["line1_x"] + 135 , PART2_LINE_COORD_y["line8_y"]+43),11,BLACK,"freesansbold.ttf")

    if n == 3 :

        pygame.draw.rect(SCREEN,RED,[pannel_f_x-3,pannel_f_y+102 ,320 , function_panel_height*2+20-3],2)
        text_display("Here, you can check or uncheck the ",(PART2_LINE_COORD_x["line1_x"] + 105 , PART2_LINE_COORD_y["line8_y"]+18 ),11,BLACK,"freesansbold.ttf")
        text_display("box, in order to show or hide objects  ",(PART2_LINE_COORD_x["line1_x"] + 105 , PART2_LINE_COORD_y["line8_y"]+32 ),11,BLACK,"freesansbold.ttf")
        text_display("depending on what you want. ",(PART2_LINE_COORD_x["line1_x"] + 105 , PART2_LINE_COORD_y["line8_y"]+46 ),11,BLACK,"freesansbold.ttf")

    if n == 4:
        pygame.draw.rect(SCREEN,RED,[pannel_f_x-38,pannel_f_y+197 ,373 , function_panel_height*4+20],2)
        text_display("This is obviously the keyboard ",(PART2_LINE_COORD_x["line1_x"] + 105 , PART2_LINE_COORD_y["line8_y"]+18 ),11,BLACK,"freesansbold.ttf")
        text_display("you'll use to enter the functions. ",(PART2_LINE_COORD_x["line1_x"] + 105 , PART2_LINE_COORD_y["line8_y"]+32 ),11,BLACK,"freesansbold.ttf")

    if n == 5:
        text_display("This is the end of the tutorial ! ",(PART2_LINE_COORD_x["line1_x"] + 105 , PART2_LINE_COORD_y["line8_y"]+18 ),11,BLACK,"freesansbold.ttf")
        text_display("Lets get started ! ",(PART2_LINE_COORD_x["line1_x"] + 105 , PART2_LINE_COORD_y["line8_y"]+32 ),11,BLACK,"freesansbold.ttf")

    color_text = BLACK   
    if string_fx == "puis(x,2/3)+sqrt(1-x**2)" and string_gx == "puis(x,2/3)-sqrt(1-x**2)" and execute_f and execute_g:
        MESSAGE = "OH.. I love you too <3 !"
        
        color_text = RED

    if n > 5 :
        text_display(MESSAGE,(PART2_LINE_COORD_x["line1_x"] + 105 , PART2_LINE_COORD_y["line8_y"]+18 ),11,color_text,"freesansbold.ttf")

    
    
    #Update the screen every time we loop
    pygame.display.update()
    #Set up the speed of the loop
    clock.tick(FPS)


#Desinitilize pygame module
pygame.quit()
quit
