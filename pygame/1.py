from tkinter import W
import pygame

pygame.init()
screen_width=400
screen_height=400
screen=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Hra") #Nastavení jména té aplikace

background=(255,0,0)
background1=(0,255,0)
color=(255,0,0)

running=True

screen.fill(color)
pygame.display.flip() #pro nastavení barvy

clock=pygame.time.Clock() #defaultní nastavení fps

image=pygame.image.load("OIP.jpg") #obrázrk
image_rect=image.get_rect()


while running:
    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    if keys[pygame.K_DOWN]:

    

        if color==(255,0,0):
            color=(0,255,0)
        else:
            color=(255,0,0)
    if keys[pygame.K_UP]:
        image_rect.x+=1
        

    

    screen.fill(color)

    pygame.draw.rect(screen,(0,0,255),pygame.Rect(30,30,350,60))

    screen.blit(image,image_rect)

    #set_colorkey udělá transparentní pozadí pygame.Surface.set_colorkey (image, [255,255,255])
    #průhlednost se dá přenastavit pomocí surface.set_alpha()

    

    pygame.display.update() #překreslí celou obrazovku na aktuální parametry



    clock.tick(60) #nastavení fps

    
