"""import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((600, 600))
window.fill((255, 255, 255))

# List to store triangle vertices
triangle_vertices = []

# Color of the triangle
triangle_color = (0, 0, 255)

# Counter for number of clicks
click_counter = 0

run = True

while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        elif event.type == MOUSEBUTTONDOWN:
            # Get the position of the mouse cursor
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Add vertex to the list of triangle vertices
            triangle_vertices.append((mouse_x, mouse_y))
            # Increment click counter
            click_counter += 1

    # If three clicks have been made, draw the triangle
    if click_counter == 4: #lze to udělat i přes modulo 4 toho listu bodů, abych měl jistotu, že tam mám další 4 body 4,8,12 apod.
        pygame.draw.polygon(window, triangle_color, triangle_vertices)
        # Reset click counter and triangle vertices list
        click_counter = 0
        triangle_vertices = []

    pygame.display.update() #lze to vložit i do ifu, aby se tak dělo pouze v případě změny

pygame.quit()


#Pro kreslení obdélníku se využívá pygame.draw.rect, je nutné specifikovat na co to vykreslit, což je proměnná window, poté je nutné specifikovat barvy a souřadnice rohu, poslední číslo dává tloušťku obvodu, což způsobí že obdélník nebude mít vybarvený obsah
#pygame.draw.rect(window,barva,pozice,tloustka)
#Poslední souřadnicí u rect lze také specifikovat zaoblení rohu pomocí čtyř čísel, čím větší číslo, tím větší zaoblení
#Pro kreslení kruhu se používá pygame.draw.circle pygame.draw.circle(window, barva, souradnice středu, poloměr kružnice, její tloušťka - tloušťka obvodu)
#Pro kreslení mnohoúhelníku se používá pygame.draw.polygon(window, barva, [specifikace bodů - záleží na jejich pořadí],tloušťka či zahlé rohy)"""
"""
#Vlastní akce

import pygame

#Pygame.quit a mousebuttondown 

import pygame 
  
  
pygame.init() 
  
# Setting up the screen and timer 
screen = pygame.display.set_mode((500, 500)) 
timer = pygame.time.Clock() 
  
# set title 
pygame.display.set_caption('Custom Events') 
  
# defining colours 
WHITE = (255, 255, 255) 
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
  
# Keep a track of active variable 
bg_active_color = WHITE 
screen.fill(WHITE) 
  
# custom user event to change color 
CHANGE_COLOR = pygame.USEREVENT + 1
  
# custom user event to inflate defalte 
# box 
ON_BOX = pygame.USEREVENT + 2
  
# creating Rectangle 
box = pygame.Rect((225, 225, 50, 50)) 
grow = True
  
# posting a event to switch color after  
# every 500ms 
pygame.time.set_timer(CHANGE_COLOR, 500) #Toto změní barvu každou půlvteřinu, change_color reprezentuje tu uživatelskou událost - DŮLEŽITÉ 
  
running = True
while running: 
    
    # checks which all events are posted 
    # and based on that perform required 
    # operations 
    for event in pygame.event.get(): 
        
        # switching colours after every 
        # 500ms 
        if event.type == CHANGE_COLOR: 
            if bg_active_color == GREEN: 
                screen.fill(GREEN) 
                bg_active_color = WHITE 
            elif bg_active_color == WHITE: 
                screen.fill(WHITE) 
                bg_active_color = GREEN 
  
        if event.type == ON_BOX:
            
            # to inflate and deflate box 
            if grow: 
                box.inflate_ip(3, 3) #Při najetí na čtverec se zvětší o 3 pixely vždy, když na něj najedeme až do šířky 75 px
                grow = box.width < 150
            else: 
                box.inflate_ip(-3, -3) 
                grow = box.width < 50
  
        if event.type == pygame.QUIT: 
            
            # for quitting the program 
            running = False
  
    # Posting event when the cursor is on top  
    # of the box 
    if box.collidepoint(pygame.mouse.get_pos()): 
        pygame.event.post(pygame.event.Event(ON_BOX)) #Post znamená, že to někam pošle - do těch eventů - DŮLEŽITÉ
  
    # Drawing rectangle on the screen 
    pygame.draw.rect(screen, RED, box) 
  
    # Updating Screen 
    pygame.display.update() 
      
    # Setting Frames per Second 
    timer.tick(30) 
  
pygame.quit() """

#Input z klávesnice


"""# importing pygame module
import pygame
 
# importing sys module
import sys
 
# initialising pygame
pygame.init()
 
# creating display
display = pygame.display.set_mode((300, 300))
 
# creating a running loop
while True:
       
    # creating a loop to check events that
    # are occurring
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
        # checking if keydown event happened or not
        if event.type == pygame.KEYDOWN: #Zjišťujeme speciální event KEYDOWN
           
            # if keydown event happened
            # than printing a string to output
            print("A key has been pressed")"""

"""K_BACKSPACE	backspace
K_TAB	tab
K_CLEAR	clear
K_RETURN	return
K_PAUSE	pause
K_ESCAPE	escape
K_SPACE	space
K_EXCLAIM	exclaim
K_HASH	hash
K_QUOTEDBL	quotedbl
K_DOLLAR	dollar
K_AMPERSAND	ampersand
K_QUOTE	quote
K_LEFTPAREN	left parenthesis
K_RIGHTPAREN	right parenthesis
K_ASTERISK	asterisk
K_PLUS	plus sign
K_COMMA	comma
K_MINUS	 minus sign
K_PERIOD 	period
K_SLASH	forward slash
K_0 	0
K_1	1
K_2	2
K_3	3
K_4	4
K_5	5
K_6	6
K_7	7
K_8	8
K_9	9
K_COLON	colon
K_SEMICOLON	semicolon
K_LESS	less-than sign
K_EQUALS	equals sign
K_GREATER	greater-than sign
K_QUESTION 	question mark
K_AT	at
K_LEFTBRACKET	left bracket
K_BACKSLASH 	backslash
K_RIGHTBRACKET  	right bracket
K_CARET	caret
K_UNDERSCORE	underscore
K_BACKQUOTE	grave
K_a,b,c…….z	A to Z Alphabet
K_DELETE	delete
K_KP0, K_KP1, K_KP2….K_KP9	keypad 0 to 9
K_KP_PERIOD	keypad period
K_KP_DIVIDE	keypad divide
K_KP_MULTIPLY	keypad multiply
K_KP_MINUS	keypad minus
K_KP_PLUS  	keypad plus
K_KP_ENTER	keypad enter
K_KP_EQUALS	keypad equals
K_UP	up arrow
K_DOWN	down arrow
K_RIGHT 	right arrow
K_LEFT  	Left arrow
K_INSERT	Insert
K_HOME	Home
K_END	End
K_PAGEUP 	Page Up
K_PAGEDOWN  	Page Down
K_F1, K_F2, K_F3……K_F15	F1 to F15
K_NUMLOCK	Numlock
K_CAPSLOCK	Capsloack
K_SCROLLOCK	Scrollock
K_RSHIFT	Right shift
K_LSHIFT	Left shift
K_RCTRL	right control
K_LCTRL	Left control
K_RALT 	Right alt
K_LALT 	Left alt
K_RMETA	right meta
K_LMETA 	left meta
K_LSUPER	left Windows key
K_RSUPER 	right Windows key
K_MODE	mode shift
K_HELP	Help
K_PRINT	Print Screen
K_SYSREQ	sysrq
K_BREAK	Break
K_MENU	Menu
K_POWER	Power
K_EURO	Euro"""


""""# importing pygame module
import pygame
 
# importing sys module
import sys
 
# initialising pygame
pygame.init()
 
# creating display
display = pygame.display.set_mode((300, 300))
 
# creating a running loop
while True:
       
    # creating a loop to check events that 
    # are occurring
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
        # checking if keydown event happened or not
        if event.type == pygame.KEYDOWN:
               
            # checking if key "A" was pressed
            if event.key == pygame.K_a:
                print("Key A has been pressed")
                display.fill((255,0,0))
               
            # checking if key "J" was pressed
            if event.key == pygame.K_j:
                print("Key J has been pressed")
                display.fill((0,255,0))
               
            # checking if key "P" was pressed
            if event.key == pygame.K_p:
                print("Key P has been pressed")
             
            # checking if key "M" was pressed
            if event.key == pygame.K_m:
                print("Key M has been pressed")
        pygame.diplay.update()"""

#Práce s textem

"""# import pygame
import pygame
 
# initializing pygame
pygame.font.init()
 
# check whether font is initialized
# or not
pygame.font.get_init()
 
# create the display surface
display_surface = pygame.display.set_mode((500, 500))
 
# change the window screen title
pygame.display.set_caption('Our Text')
 
# Create a font file by passing font file
# and size of the font
font1 = pygame.font.SysFont('Comic Sans MS', 50) #Nejdříve je nutné načíst font - nejdříve font a pak velikost
font2 = pygame.font.SysFont('chalkduster.ttf', 40)
 
# Render the texts that you want to display
text1 = font1.render('Obamna', True, (0, 255, 0)) #Toto je samotný text - nejdříve je font, poté jeho zobrazení na true a barva
text2 = font2.render('GeeksForGeeks', True, (0, 255, 0))

 
# create a rectangular object for the
# text surface object
textRect1 = text1.get_rect() #Je nutné z něj udělat rectangle, aby mohl kolidovat apod.
textRect2 = text2.get_rect()
 
# setting center for the first text
textRect1.center = (250, 250)
 
# setting center for the second text
textRect2.center = (250, 300) #Nastavení souřadnic středu toho celkového rectu, kdyby to bylo 0,0 - je to v levém horním rohu
#Kdyby se tam nepsal center, bralo by se to od horního levého rohu daného rectu
 
while True:
 
    # add background color using RGB values
    display_surface.fill((255, 0, 0))
 
    # copying the text surface objects
    # to the display surface objects
    # at the center coordinate.
    display_surface.blit(text1, textRect1) #Je nutné zde vždy uvést samotný text a potom ten rect, v němž text je
    display_surface.blit(text2, textRect2)
 
    # iterate over the list of Event objects
    # that was returned by pygame.event.get()
    # method.
    for event in pygame.event.get():
 
        if event.type == pygame.QUIT:
           
            # deactivating the pygame library
            pygame.quit()
 
            # quitting the program.
            quit()
 
        # update the display
        pygame.display.update()"""

"""# import pygame module
import pygame
 
# import sys library
import sys
 
# initializing pygame
pygame.init()
 
clock = pygame.time.Clock()
 
# Set the window screen size
display_screen = pygame.display.set_mode((500, 500))
 
# add font style and size
base_font = pygame.font.Font(None, 40)
 
 
# stores text taken by keyboard
user_text = ''
 
# set left, top, width, height in 
# Pygame.Rect()
input_rect = pygame.Rect(200, 200, 140, 32)
color_active = pygame.Color("blue")
color_passive = pygame.Color("gray15")
color = color_passive
 
active = False
 
while True:
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
        # when mouse collides with the rectangle
        # make active as true
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            if not input_rect.collidepoint(event.pos):
                active=False
 
        # if the key is physically pressed down
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_BACKSPACE:
                 
                # stores text except last letter
                user_text = user_text[0:-1]
            else:
                user_text += event.unicode
 
    display_screen.fill((0, 0, 0))
 
    if active:
        color = color_active
    else:
        color = color_passive
 
    pygame.draw.rect(display_screen, color, input_rect)
     
    # render the text
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    display_screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = max(100, text_surface.get_width() + 10)
    pygame.display.flip()
    clock.tick(60)"""

"""import pygame

import sys

pygame.init()


# Set the window screen size
screen = pygame.display.set_mode((500, 500))

# add font style and size
base_font = pygame.font.Font(None, 40)

clock=pygame.time.Clock()

time=str(10)

time_text=base_font.render(time,True,(255,0,0))

time_text_rect=time_text.get_rect()

while True:
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            time=int(time)+5
            time=str(time)
        if int(time)<=0:
            pygame.quit()
            sys.exit()
        screen.fill((0,0,0))
        time_text=base_font.render(time,True,(255,0,0))
        screen.blit(time_text,time_text_rect)
        clock.tick(1)
        time=int(time)-1
        time=str(time)
        pygame.display.update()"""

#Text box v pygame

"""# import sys module 
import pygame 
import sys 
  
  
# pygame.init() will initialize all 
# imported module 
pygame.init() 
  
clock = pygame.time.Clock() 
  
# it will display on screen 
screen = pygame.display.set_mode([600, 500]) 
  
# basic font for user typed 
base_font = pygame.font.Font(None, 32) 
user_text = '' 
  
# create rectangle 
input_rect = pygame.Rect(200, 200, 140, 32) 
  
# color_active stores color(lightskyblue3) which 
# gets active when input box is clicked by user 
color_active = pygame.Color('lightskyblue3') 
  
# color_passive store color(chartreuse4) which is 
# color of input box. 
color_passive = pygame.Color('chartreuse4') 
color = color_passive 
  
active = False
  
while True: 
    for event in pygame.event.get(): 
  
      # if user types QUIT then the screen will close 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit() 
  
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if input_rect.collidepoint(event.pos): 
                active = True
            else: 
                active = False
  
        if event.type == pygame.KEYDOWN: 
  
            # Check for backspace 
            if event.key == pygame.K_BACKSPACE: 
  
                # get text input from 0 to -1 i.e. end. 
                user_text = user_text[:-1] 
  
            # Unicode standard is used for string 
            # formation 
            else: 
                user_text += event.unicode
      
    # it will set background color of screen 
    screen.fill((255, 255, 255)) 
  
    if active: 
        color = color_active 
    else: 
        color = color_passive 
          
    # draw rectangle and argument passed which should 
    # be on screen 
    pygame.draw.rect(screen, color, input_rect) 
  
    text_surface = base_font.render(user_text, True, (255, 255, 255)) 
      
    # render at position stated in arguments 
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
      
    # set width of textfield so that text cannot get 
    # outside of user's text input 
    input_rect.w = max(100, text_surface.get_width()+10) 
      
    # display.flip() will update only a portion of the 
    # screen to updated, not full area 
    pygame.display.flip() 
      
    # clock.tick(60) means that for every second at most 
    # 60 frames should be passed. 
    clock.tick(60) """


#Obrázky v pygame

"""# importing required library
import pygame
 
# activate the pygame library .
pygame.init()
X = 600
Y = 600
 
# create the display surface object
# of specific dimension..e(X, Y).
scrn = pygame.display.set_mode((X, Y))
 
# set the pygame window name
pygame.display.set_caption('image')
 
# create a surface object, image is drawn on it.
imp = pygame.image.load("H:\\5421603-200.png")
 
# Using blit to copy content from one surface to other
scrn.blit(imp, (0, 0))
 
# paint screen one time
pygame.display.flip()
status = True
while (status):
 
  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
    for i in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False
 
# deactivates the pygame library
pygame.quit()
"""

#Výška a šířka obrázku

"""import pygame as py 
  
# Initiate pygame and the modules that comes with pygame 
py.init() 
  
# setting frame/window/surface with some dimensions 
window = py.display.set_mode((300, 300)) 
  
# to set title of pygame window 
py.display.set_caption("GFG") 
  
# creating image object 
image = py.image.load('/home/amninder/Pictures/Wallpapers/download.png') 
  
# to display size of image 
print("size of image is (width,height):", image.get_size()) 
  
# loop to run window continuously 
while True: 
    window.blit(image, (0, 0)) 
  
    # loop through the list of Event 
    for event in py.event.get(): 
        # to end the event/loop 
        if event.type == py.QUIT: 
  
            # it will deactivate the pygame library 
            py.quit() 
            quit() 
  
        # to display when screen update 
        py.display.flip() 

# import pygame 
import pygame 
  
# creating image object 
image = pygame.image.load('/home/amninder/Pictures/Wallpapers/download.png') 
  
# get_height method return the height of the surface pixel, 
# in our case surface is image 
print("Height of image= " + str(image.get_height())) 
  
# get_width method return the width of the surface pixel, 
# in our case surface is image 
print("Width of image= " + str(image.get_width())) """

#Scale image a rotace obrázku


"""# Import pygame
import pygame
 
# Initialise pygame
pygame.init()
 
# Set window size
size = width,height = 600, 600
screen = pygame.display.set_mode(size)
 
# Clock
clock = pygame.time.Clock()
 
# Load image
image = pygame.image.load('gfg.png')
 
# Set the size for the image
DEFAULT_IMAGE_SIZE = (200, 200)
 
# Scale the image to your needed size
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE) #Tento příkaz budeme velice často používat
 
# Set a default position
DEFAULT_IMAGE_POSITION = (200,200)
 
# Prepare loop condition
running = False
 
# Event loop
while not running:
 
    # Close window event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
 
    # Background Color
    screen.fill((0, 0, 0))
 
    # Show the image
    screen.blit(image, DEFAULT_IMAGE_POSITION)
 
    # Part of event loop
    pygame.display.flip()
    clock.tick(30)"""

"""# Import pygame
import pygame
 
# Initialise pygame
pygame.init()
 
# Set window size
size = width,height = 600, 600
screen = pygame.display.set_mode(size)
 
# Clock
clock = pygame.time.Clock()
 
# Load image
image = pygame.image.load('gfg.png')
 
# Set the size for the image
DEFAULT_IMAGE_SIZE = (200, 200)
 
# Rotate the image by any degree
image = pygame.transform.rotate(image, 180)
 
# Set a default position
DEFAULT_IMAGE_POSITION = (200,200)
 
# Prepare loop condition
running = False
 
# Event loop
while not running:
 
    # Close window event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
 
    # Background Color
    screen.fill((0, 0, 0))
 
    # Show the image
    screen.blit(image, DEFAULT_IMAGE_POSITION)
 
    # Part of event loop
    pygame.display.flip()
    clock.tick(30)
"""

#Úkol k roatci a scalování obrázku
"""import pygame

pygame.init()

screen_width=1000
screen_height=500

screen=pygame.display.set_mode((screen_width,screen_height))

circle_x=0
circle_y=screen_height//2-60

left=False

run=True

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    if left:
        circle_x-=1
    else:
        circle_x+=1
        
    screen.fill((0,0,0))
    pygame.draw.line(screen, (255,0,0), (0,screen_height//2),(screen_width,screen_height//2))
    pygame.draw.circle(screen, (0, 255, 0),[circle_x,circle_y], 60, 0)
    if circle_x+60>=screen_width:
        left=True
    if circle_x-60<=0:
        left=False

    pygame.display.update()

    print(left)

pygame.quit()"""

#varianta s míčem

import pygame

pygame.init()

screen_width=1000
screen_height=500

screen=pygame.display.set_mode((screen_width,screen_height))

circle_x=0
circle_y=screen_height//2-50

ball=pygame.image.load("Sports-Ball-Transparent.png")
ball=pygame.transform.scale(ball,(100,100))

ball_rect=ball.get_rect()

ball_rect.center=(circle_x,circle_y)

left=False

run=True

rotation_angle=0

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    if left:
        circle_x-=0.2
        rotation_angle+=0.2
    else:
        circle_x+=0.2
        rotation_angle-=0.2
        
    screen.fill((0,0,0))
    pygame.draw.line(screen, (255,0,0), (0,screen_height//2),(screen_width,screen_height//2))
    if circle_x+50>=screen_width:
        left=True
    if circle_x-50<=0:
        left=False

    old_center_x=circle_x
    old_center_y=circle_y

    new_ball=pygame.transform.rotate(ball,rotation_angle)
    
    ball_rect=new_ball.get_rect()

    ball_rect.center=(old_center_x,old_center_y)

    screen.blit(new_ball,ball_rect)
    
    pygame.display.flip()

pygame.quit()
        


      
