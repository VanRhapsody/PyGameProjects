import pygame
from Block import * #importuntí třídy Block
from Player import * #import třídy Player

pygame.init()

screen_width=800
screen_height=800

screen=pygame.display.set_mode((screen_width,screen_height))
clock=pygame.time.Clock()
run=True

width,height=screen.get_size()

block=Block("H:\\a IT3 programování\\pygame\\uhybanibloku\\image\\60726108c2da773edf6afc9e30bc591f.png",) #Vytvoření instance objektu

group=pygame.sprite.Group() #Vytvoření group pro blocky

player=Player("H:\\a IT3 programování\\pygame\\uhybanibloku\\image\\Steve_(Minecraft).png",screen_width/2,50,5)



while run:
    clock.tick(25)
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
    pygame.display.update()

pygame.quit()



