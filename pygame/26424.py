import pygame

#Nastavení hranic hry 

"""
# importing the modules 
import pygame 
import random 
   
# instantiating the class 
pygame.init() 
    
# dimension of the screen 
width = 700
height = 550
    
# colours 
white = (255, 255, 255) 
red = (255, 0, 0) 
green = (0, 255, 0) 
blue = (0, 0, 255) 
black = (0, 0, 0) 
    
# creating a Screen 
screen = pygame.display.set_mode((width, height)) 
   
# title of the screen 
pygame.display.set_caption("Bouncy Ball") 
  
# declaring variables for the ball 
ball_X = width/2 - 12
ball_Y = height/2 - 12
ball_XChange = 3* random.choice((1, -1)) #Na začátku programu půjde buď doleva či doprava
ball_YChange = 3
ballPixel = 24
   
# gaming Loop 
running = True
while running: 
   
    # background color 
    screen.fill(red) 
   
    # to exit the loop 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
  
    # bouncing the ball 
    if ball_X + ballPixel >= width or ball_X <= 0: #Když je ta x souřadnice větší než screen width či menší než 0, nastaví se opačný směr vodorovný
        ball_XChange *= -1
    if ball_Y + ballPixel >= height or ball_Y <= 0: #To je to stejné jako u x souřadnice
        ball_YChange *= -1
       
    # moving the ball 
    ball_X += ball_XChange 
    ball_Y += ball_YChange 
  
    # drawing the ball 
    ballImg = pygame.draw.circle(screen, (0,0,255), 
                                 (int(ball_X), int(ball_Y)), 
                                 15) 
    pygame.display.update() """

#Detekce kolizí

"""
# define a function for 
# collision detection
def crash():
  # take a global variable
  global blockYPosition
 
  # check conditions
  if playerYPosition < (blockYPosition + pixel):
 
      if ((playerXPosition > blockXPosition 
           and playerXPosition < (blockXPosition + pixel))
          or ((playerXPosition + pixel) > blockXPosition
           and (playerXPosition + pixel) < (blockXPosition + pixel))):
 
          blockYPosition = height + 1000"""

#Sprite

#Je to objekt, ve většině případů obrázek


import pygame 
  
"""# GLOBAL VARIABLES 
COLOR = (255, 100, 98) 
SURFACE_COLOR = (167, 255, 100) 
WIDTH = 500
HEIGHT = 500
  
# Object class 
class Sprite(pygame.sprite.Sprite): #Dědí od třídy Sprite, což umožňuje práci s group
    def __init__(self, color, height, width): 
        super().__init__() #super značí poděděnou třídu, ty lze to nahradit označením pro sprite
  
        self.image = pygame.Surface([width, height]) #Vrátí plochu o daných rozměrech
        self.image.fill(SURFACE_COLOR) #Vybarví ten surface
        self.image.set_colorkey(COLOR) 
  
        pygame.draw.rect(self.image, 
                         color, 
                         pygame.Rect(0, 0, width, height)) 
  
        self.rect = self.image.get_rect() """

        
import pygame 
import random 
  
"""# GLOBAL VARIABLES 
COLOR = (255, 100, 98) 
SURFACE_COLOR = (167, 255, 100) 
WIDTH = 500
HEIGHT = 500
  
# Object class 
class Sprite(pygame.sprite.Sprite): 
    def __init__(self, color, height, width): 
        super().__init__() 
  
        self.image = pygame.Surface([width, height]) 
        self.image.fill(SURFACE_COLOR) 
        self.image.set_colorkey(COLOR) 
  
        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height)) 
  
        self.rect = self.image.get_rect() 
  
  
pygame.init() 
  
RED = (255, 0, 0) 
  
size = (WIDTH, HEIGHT) 
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Creating Sprite") 
  
all_sprites_list = pygame.sprite.Group() #Toto je vytvoření té skupiny
#Ve hře totiž budeme mít hodně prvků a můžeme je dát do jedné skupiny pro snadnější práci s nimi
  
object_ = Sprite(RED, 20, 30) #Vytváříme instanci třídy Sprite
object_.rect.x = 200
object_.rect.y = 300
  
all_sprites_list.add(object_) #Přidání objektu do té groupy
  
exit = True
clock = pygame.time.Clock() 
  
while exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = False
  
    all_sprites_list.update() #Aktualizace té group
    #Na všech prvcích v group se zavolá metoda update, která má být definována pro daný objekt
    screen.fill(SURFACE_COLOR) 
    all_sprites_list.draw(screen) #Vykreslí objekty v třídě
    #Udělá to draw pro všechny objekty, ale ty objekty to musí mít definováno
    pygame.display.flip() 
    #Flip updatne celou obrazovku, update obnoví jen prvky, které se změnily
    clock.tick(60) 
  
pygame.quit() """

#Kontrola sprite



"""import random
import pygame
 
# Global Variables
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500
 
# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)
 
        pygame.draw.rect(self.image,
                         color,
                         pygame.Rect(0, 0, width, height))
 
        self.rect = self.image.get_rect() #Tento rect se musí posouvat, neposouvají se samotné obrázky
        #Pak se už pracuje pouze s tím rectanglem
 
    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
 
    def moveForward(self, speed):
        self.rect.y += speed * speed/10
 
    def moveBack(self, speed):
        self.rect.y -= speed * speed/10
 
 
pygame.init()
 
 
RED = (255, 0, 0)
 
 
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating Sprite")
 
 
all_sprites_list = pygame.sprite.Group()
 
playerCar = Sprite(RED, 20, 30) #Toto je opět instance třídy Sprite
playerCar.rect.x = 200
playerCar.rect.y = 300
 
 
all_sprites_list.add(playerCar)
 
exit = True
clock = pygame.time.Clock()
 
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(10)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(10)
    if keys[pygame.K_DOWN]:
        playerCar.moveForward(10)
    if keys[pygame.K_UP]:
        playerCar.moveBack(10)
 
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()"""


"""
import pygame
import random
import sys
 
 
# initializing the constructor
pygame.init()
 
# setting up variable screen
screen = pygame.display.set_mode((720,720))
 
# three arguments of the color tuple
c1 = random.randint(0,255)
c2 = random.randint(0,255)
c3 = random.randint(0,255)
 
# setting up variable clock
clock = pygame.time.Clock()
 
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
             
    # increases the shade of
    # the current color
    if 0 < c1 < 255:
        c1 += 1
         
    # if value of c1 exceeds 
    # 255 it resets it to 0
    elif c1 >= 255:
        c1 -= 255
         
    # if value of c1 precedes 0
    # it is incremented by 3
    elif c1 <= 0:
        c1 += 3
         
    # sets game fps to 60
    clock.tick(60)
     
    # sets bg color to tuple
    # (c1,c2,c3)
    screen.fill((c1,c2,c3)) #Tyto tři argumenty zaručují ten přechod
     
    # updates the frames of 
    # the game 
    pygame.display.update()"""

#Hudba v pygame

"""from pygame import mixer 
  
# Starting the mixer 
mixer.init() 
  
# Loading the song 
mixer.music.load("song.mp3") 
  
# Setting the volume 
mixer.music.set_volume(0.7) 
  
# Start playing the song 
mixer.music.play() 
  
# infinite loop 
while True: 
      
    print("Press 'p' to pause, 'r' to resume") 
    print("Press 'e' to exit the program") 
    query = input("  ") 
      
    if query == 'p': 
  
        # Pausing the music 
        mixer.music.pause()      
    elif query == 'r': 
  
        # Resuming the music 
        mixer.music.unpause() 
    elif query == 'e': 
  
        # Stop the mixer 
        mixer.music.stop() 
        break"""

