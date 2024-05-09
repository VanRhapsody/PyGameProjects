"""import pygame

color=(255,0,0)
a=50
b=200

screen_width=500
screen_height=500

screen=pygame.display.setmode((screen_width,screen_height))

ball=pygame.image.load("Sports-Ball-Transparent.png")
ball=pygame.transorm.scale(ball,(40,40))
rotated_ball=ball
rotation_angle=0

switch=False

run=True

while run:
    clock.tick(60)
    screen.fill((0,0,0))
    for event in pygame.event.get:
        if event.type==pygame.QUIT:
            run=False
    rotated_ball=pygame.transform.rotate(ball,rotation_angle)
    ball_rect=rotated_ball.get_rect(center=(a,b)) #Získáme otočený míč, ale musíme to uložit do původního rectu se souřadicemi v a,b aby se neposouval pryč
    #screen.blit(image1,(25,100))
    screen.blit(rotated_ball,ball_rect)
    pygame.draw.circle(screen,(255,255,255),(a,b),20)
    if switch==False and a > 350:
        switch=True
    elif switch==True and a < 45:
        switch=False
    if switch==True:
        a-=1
        rotation_angle+=1
    else:
        a+=1
        rotation_angle-=1

    pygame.draw.rect(screen,(255,0,0),pygame.Rect(30,60,30,60))"""

#Custom eventy
"""
# Python program to add Custom Events 
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
pygame.time.set_timer(CHANGE_COLOR, 500) 
  
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
                box.inflate_ip(3, 3) #Ten box se zvětšuje do doby, než je jeho šířka větší než 75 px
                grow = box.width < 75 
            else: 
                box.inflate_ip(-3, -3) 
                grow = box.width < 50 #Stejná věc jako u šířky
  
        if event.type == pygame.QUIT: 
            
            # for quitting the program 
            running = False
  
    # Posting event when the cursor is on top  
    # of the box 
    if box.collidepoint(pygame.mouse.get_pos()): 
        pygame.event.post(pygame.event.Event(ON_BOX)) 
  
    # Drawing rectangle on the screen 
    pygame.draw.rect(screen, RED, box) 
  
    # Updating Screen 
    pygame.display.update() 
      
    # Setting Frames per Second 
    timer.tick(30) 
  
pygame.quit() """

#Key eventy
"""

# importing pygame module
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
               
            # checking if key "J" was pressed
            if event.key == pygame.K_j:
                print("Key J has been pressed")
               
            # checking if key "P" was pressed
            if event.key == pygame.K_p:
                print("Key P has been pressed")
             
            # checking if key "M" was pressed
            if event.key == pygame.K_m:
                print("Key M has been pressed")"""

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
font1 = pygame.font.SysFont('freesanbold.ttf', 50)
font2 = pygame.font.SysFont('chalkduster.ttf', 40)
 
# Render the texts that you want to display
text1 = font1.render('GeeksForGeeks', True, (0, 255, 0))
text2 = font2.render('GeeksForGeeks', True, (0, 255, 0))
 
# create a rectangular object for the
# text surface object
textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
 
# setting center for the first text
textRect1.center = (250, 250)
 
# setting center for the second text
textRect2.center = (250, 300)
 
while True:
 
    # add background color using RGB values
    display_surface.fill((255, 0, 0))
 
    # copying the text surface objects
    # to the display surface objects
    # at the center coordinate.
    display_surface.blit(text1, textRect1)
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

#Obracení obrázku

"""
# import pygame and sys 
import pygame 
import sys 
  
from pygame.locals import *
  
# pygame.init() will initialize all 
# imported module 
pygame.init() 
pygame.display.set_caption('GeeksforGeeks') 
  
# screen size will display on screen 
screen = pygame.display.set_mode((600, 400), 0, 32) 
  
# pygame.image.load() will return the 
# object that has image 
img = pygame.image.load('image.png') 
  
while True: 
      
    # Background color 
    screen.fill((255, 255, 255)) 
      
    # image copy 
    img_copy = img.copy() 
      
    # pygame.transform.flip() will flip the image 
    img_with_flip = pygame.transform.flip(img_copy, True, False) 
      
    # surface.blit() function draws a source  
    # Surface onto this Surface. 
    screen.blit(img_with_flip, (50 + 1 * 120, 100)) 
      
    # event listener to quit screen 
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit() 
            sys.exit() 
  
    # update the frame per second 
    pygame.display.update() """

#Hýbání s obrázkem
"""
# Python program to move the image
# with the mouse
 
# Import the library pygame
import pygame
from pygame.locals import *
 
# Take colors input
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
 
# Construct the GUI game
pygame.init()
 
# Set dimensions of game GUI
w, h = 640, 350
screen = pygame.display.set_mode((w, h))
 
# Take image as input
img = pygame.image.load("Sports-Ball-Transparent.png")
img.convert()
 
# Draw rectangle around the image
rect = img.get_rect()
rect.center = w//2, h//2
 
# Set running and moving values
running = True
moving = False
 
# Setting what happens when game 
# is in running state
while running:
     
    for event in pygame.event.get():
 
        # Close if the user quits the 
        # game
        if event.type == QUIT:
            running = False
 
        # Making the image move
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
 
        # Set moving as False if you want 
        # to move the image only with the 
        # mouse click
        # Set moving as True if you want 
        # to move the image without the 
        # mouse click
        elif event.type == MOUSEBUTTONUP:
            moving = False
 
        # Make your image move continuously
        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)
 
    # Set screen color and image on screen
    screen.fill(YELLOW)
    screen.blit(img, rect)
 
    # Construct the border to the image
    pygame.draw.rect(screen, BLUE, rect, 2)
 
    # Update the GUI pygame
    pygame.display.update()
 
# Quit the GUI game
pygame.quit()"""

#Zvětšení a rotace obrázku
"""
# Python program to transform the  
# image with the mouse 
  
#Import the libraries pygame and math 
import pygame 
import math 
from pygame.locals import *
  
# Take colors input 
RED = (255, 0, 0) 
BLACK = (0, 0, 0) 
YELLOW = (255, 255, 0) 
  
#Construct the GUI game 
pygame.init() 
  
#Set dimensions of game GUI 
w, h = 600, 440
screen = pygame.display.set_mode((w, h)) 
  
# Set running, angle and scale values 
running = True
angle = 0
scale = 1
  
# Take image as input 
img_logo = pygame.image.load('gfg_image.jpg') 
img_logo.convert() 
  
# Draw a rectangle around the image 
rect_logo = img_logo.get_rect() 
pygame.draw.rect(img_logo, RED, rect_logo, 1) 
  
# Set the center and mouse position 
center = w//2, h//2
mouse = pygame.mouse.get_pos() 
  
#Store the image in a new variable 
#Construct the rectangle around image 
img = img_logo 
rect = img.get_rect() 
rect.center = center 
  
# Setting what happens when game is 
# in running state 
while running: 
    for event in pygame.event.get(): 
  
        # Close if the user quits the game 
        if event.type == QUIT: 
            running = False
  
        # Set at which angle the image will 
        # move left or right 
        if event.type == KEYDOWN: 
            if event.key == K_ra: 
                if event.mod & KMOD_SHIFT: 
                    angle -= 5
                else: 
                    angle += 5
  
            # Set at what ratio the image will 
            # decrease or increase 
            elif event.key == K_sa: 
                if event.mod & KMOD_SHIFT: 
                    scale /= 1.5
                else: 
                    scale *= 1.5
                  
        # Move the image with the specified coordinates, 
        # angle and scale         
        elif event.type == MOUSEMOTION: 
            mouse = event.pos 
            x = mouse[0] - center[0] 
            y = mouse[1] - center[1] 
            d = math.sqrt(x ** 2 + y ** 2) 
            angle = math.degrees(-math.atan2(y, x)) 
            scale = abs(5 * d / w) 
            img = pygame.transform.rotozoom(img_logo, angle, scale) 
            rect = img.get_rect() 
            rect.center = center 
      
    # Set screen color and image on screen 
    screen.fill(YELLOW) 
    screen.blit(img, rect) 
  
    # Draw the rectangle, line and circle through 
    # which image can be transformed  
    pygame.draw.rect(screen, BLACK, rect, 3) 
    pygame.draw.line(screen, RED, center, mouse, 2) 
    pygame.draw.circle(screen, RED, center, 6, 1) 
    pygame.draw.circle(screen, BLACK, mouse, 6, 2) 
      
    # Update the GUI game 
    pygame.display.update() 
  
# Quit the GUI game 
pygame.quit()
    """

#Činnost při kliknutí na tlačítko
"""

import pygame 
import sys 
  
  
# initializing the constructor 
pygame.init() 
  
# screen resolution 
res = (720,720) 
  
# opens up a window 
screen = pygame.display.set_mode(res) 
  
# white color 
color = (255,255,255) 
  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100) 
  
# stores the width of the 
# screen into a variable 
width = screen.get_width() 
  
# stores the height of the 
# screen into a variable 
height = screen.get_height() 
  
# defining a font 
smallfont = pygame.font.SysFont('Corbel',35) 
  
# rendering a text written in 
# this font 
text = smallfont.render('quit' , True , color) 
  
while True: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                pygame.quit() 
                  
    # fills the screen with a color 
    screen.fill((60,25,60)) 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade  
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40]) 
      
    # superimposing the text onto our button 
    screen.blit(text , (width/2+50,height/2)) 
      
    # updates the frames of the game 
    pygame.display.update() """

#Kreslení pomocí klávesnice
"""
# import pygame module in this program 
import pygame 
  
# activate the pygame library .    
# initiate pygame and give permission    
# to use pygame's functionality.    
pygame.init() 
  
# create the display surface object    
# of specific dimension..e(500, 500).    
win = pygame.display.set_mode((500, 500)) 
  
# set the pygame window name   
pygame.display.set_caption("Moving rectangle") 
  
# marker current co-ordinates   
x = 200
y = 200
  
# dimensions of the marker  
width = 10
height = 10
  
# velocity / speed of movement  
vel = 10
  
# Indicates pygame is running  
run = True
  
# infinite loop   
while run: 
    # creates time delay of 10ms   
    pygame.time.delay(10) 
  
    # iterate over the list of Event objects    
    # that was returned by pygame.event.get() method.    
    for event in pygame.event.get(): 
  
        # if event object type is QUIT    
        # then quitting the pygame    
        # and program both.    
        if event.type == pygame.QUIT: 
            # it will make exit the while loop 
            run = False
    # stores keys pressed   
    keys = pygame.key.get_pressed() 
  
    # if left arrow key is pressed  
    if keys[pygame.K_LEFT] and x > 0: 
        # decrement in x co-ordinate 
        x -= vel 
  
        # if left arrow key is pressed 
    if keys[pygame.K_RIGHT] and x < 500 - width: 
        # increment in x co-ordinate 
        x += vel 
  
        # if left arrow key is pressed 
    if keys[pygame.K_UP] and y > 0: 
        # decrement in y co-ordinate 
        y -= vel 
  
        # if left arrow key is pressed 
    if keys[pygame.K_DOWN] and y < 500 - height: 
        # increment in y co-ordinate  
        y += vel 
  
  
    # drawing spot on screen which is rectangle here   
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) 
  
    # it refreshes the window  
    pygame.display.update() 
  
# closes the pygame window   
pygame.quit()  """

#Kreslení pomocí myši

"""# import pygame module in this program 
import pygame 
  
# activate the pygame library .    
# initiate pygame and give permission    
# to use pygame's functionality.    
pygame.init() 
  
# create the display surface object    
# of specific dimension..e(500, 500).    
win = pygame.display.set_mode((500, 500)) 
  
# set the pygame window name   
pygame.display.set_caption("Moving rectangle") 
  
# marker current co-ordinates   
x = 200
y = 200
  
# dimensions of the marker  
width = 10
height = 10

drawing=False
  
# Indicates pygame is running  
run = True
  
# infinite loop   
while run: 
  
    # iterate over the list of Event objects    
    # that was returned by pygame.event.get() method.    
    for event in pygame.event.get(): 
  
        # if event object type is QUIT    
        # then quitting the pygame    
        # and program both.    
        if event.type == pygame.QUIT: 
            # it will make exit the while loop 
            run = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            drawing=True
        if event.type==pygame.MOUSEBUTTONUP:
            drawing=False
    if drawing:
        x,y=pygame.mouse.get_pos()
        # drawing spot on screen which is rectangle here   
        pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) 
  
    # it refreshes the window  
    pygame.display.update() 
  
# closes the pygame window   
pygame.quit() """

#Pohyb čtverce bez stálého kreslení 

"""# import pygame module in this program  
import pygame 
  
# activate the pygame library .   
# initiate pygame and give permission   
# to use pygame's functionality.   
pygame.init() 
  
# create the display surface object   
# of specific dimension..e(500, 500).   
win = pygame.display.set_mode((500, 500)) 
  
# set the pygame window name  
pygame.display.set_caption("Moving rectangle") 
  
# object current co-ordinates  
x = 200
y = 200
  
# dimensions of the object  
width = 20
height = 20
  
# velocity / speed of movement 
vel = 10
  
# Indicates pygame is running 
run = True
  
# infinite loop  
while run: 
    # creates time delay of 10ms  
    pygame.time.delay(10) 
      
    # iterate over the list of Event objects   
    # that was returned by pygame.event.get() method.   
    for event in pygame.event.get(): 
          
        # if event object type is QUIT   
        # then quitting the pygame   
        # and program both.   
        if event.type == pygame.QUIT: 
              
            # it will make exit the while loop  
            run = False
    # stores keys pressed  
    keys = pygame.key.get_pressed() 
      
    # if left arrow key is pressed 
    if keys[pygame.K_LEFT] and x>0: 
          
        # decrement in x co-ordinate 
        x -= vel 
          
    # if left arrow key is pressed 
    if keys[pygame.K_RIGHT] and x<500-width: 
          
        # increment in x co-ordinate 
        x += vel 
         
    # if left arrow key is pressed    
    if keys[pygame.K_UP] and y>0: 
          
        # decrement in y co-ordinate 
        y -= vel 
          
    # if left arrow key is pressed    
    if keys[pygame.K_DOWN] and y<500-height: 
        # increment in y co-ordinate 
        y += vel 
         
              
    # completely fill the surface object   
    # with black colour   
    win.fill((0, 0, 0)) 
      
    # drawing object on screen which is rectangle here  
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) 
      
    # it refreshes the window 
    pygame.display.update()  
  
# closes the pygame window  
pygame.quit() """

#Skákání

# import pygame module in this program  
import pygame 
   
# activate the pygame library .  
# initiate pygame and give permission  
# to use pygame's functionality.  
pygame.init() 
   
# create the display surface object  
# of specific dimension..e(500, 500).  
win = pygame.display.set_mode((500, 500)) 
   
# set the pygame window name  
pygame.display.set_caption("Jump Game") 
   
# object current co-ordinates 
x = 150
y = 250
   
# dimensions of the object 
width = 30
height = 40
   
# Stores if player is jumping or not 
isjump = False
   
# Force (v) up and mass m. 
v = 15
m = 1
   
# Indicates pygame is running 
run = True

line1=pygame.Rect(0,300,200,1)

line2=pygame.Rect(400,250,100,1)

cube=pygame.Rect(x,y,50,50)
   
# infinite loop 
while run: 
    if cube.colliderect(line1):
            # making isjump equal to false  
            isjump = False
  
            # setting original values to v and m 
            v = 15
            m = 1
            cube.bottom=300+1
    elif cube.colliderect(line2):
            # making isjump equal to false  
            isjump = False
  
            # setting original values to v and m 
            v = 15
            m = 1
            cube.bottom=250+1
    elif y==400:
            # making isjump equal to false  
            isjump = False
  
            # setting original values to v and m 
            v = 15
            m = 1
    else:
        isjump=True

   
    # completely fill the surface object  
    # with black colour  
    win.fill((0, 0, 0)) 
   
   
       
    # iterate over the list of Event objects  
    # that was returned by pygame.event.get() method.  
    for event in pygame.event.get(): 
           
        # if event object type is QUIT  
        # then quitting the pygame  
        # and program both.  
        if event.type == pygame.QUIT: 
               
            # it will make exit the while loop 
            run = False
    # stores keys pressed 
    keys = pygame.key.get_pressed() 
        
    if isjump == False: 
   
        # if space bar is pressed 
        if keys[pygame.K_SPACE]: 
                  
            # make isjump equal to True 
            isjump = True
        if keys[pygame.K_a]:
            x-=5
        if keys[pygame.K_d]:
            x+=5
               
    if isjump : 
        # calculate force (F). F = 1 / 2 * mass * velocity ^ 2. 
        F =(1 / 2)*m*(v**2) 
           
        # change in the y co-ordinate 
        y-= F 
           
        # decreasing velocity while going up and become negative while coming down 
        v = v-1
           
        # object reached its maximum height 
        if v<0: 
               
            # negative sign is added to counter negative velocity 
            m =-1
   
        # objected reaches its original state 

        keys = pygame.key.get_pressed() 

        if keys[pygame.K_a]:
            x-=5
        if keys[pygame.K_d]:
            x+=5


       
    # creates time delay of 10ms 
    pygame.time.delay(10) 

    

    pygame.draw.rect(win,(255,0,0),line1)
    pygame.draw.rect(win,(255,0,0),line2)

    # drawing object on screen which is rectangle here  
    pygame.draw.rect(win, (255, 0, 0), cube) 

    cube=pygame.Rect(x,y,50,50)
   
    # it refreshes the window 
    pygame.display.update()  
# closes the pygame window     
pygame.quit()

