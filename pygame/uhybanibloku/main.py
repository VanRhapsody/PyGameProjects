import pygame
from Block import * #importuntí třídy Block
from Player import * #import třídy Player
import random
pygame.init()

screen_width=800
screen_height=800

screen=pygame.display.set_mode((screen_width,screen_height))
clock=pygame.time.Clock() #Možnost nastavení FPS
run=True

width,height=screen.get_size()



all_block_list=pygame.sprite.Group() #Vytvoření group pro blocky, proto se v těch třídách dědí od sprite

random_x_value=random.randint(25,775)

block=Block("pygame\\uhybanibloku\\image\\Block_of_Gold_JE6_BE3.png",25,random_x_value) #Vytvoření instance dbjektu blok

player=Player("pygame\\uhybanibloku\\image\\Steve_(Minecraft).png",screen_width/2,screen_height-50,100,10) #50 na y, protože rozměry obrázku jsou 100 a umisťuje se na základě centeru

all_block_list.add(block) #Přidání bloku do group block

#User event pro další generování bloků
ADD_BLOCK=pygame.USEREVENT+1
pygame.time.set_timer(ADD_BLOCK,1000)

#Přidání textu pro skore
score=0
score_font=pygame.font.SysFont("calibri",30)
score_text=score_font.render(f"Skore: {score}",True, (255,255,255))
score_text_rect=score_text.get_rect()
score_text_rect.topright=(screen_width-50,10)

show_main_menu=True

game_background=pygame.image.load("pygame\\uhybanibloku\image\\20230803_Dresden-Nickern_178kk.jpg")
game_background_scale=pygame.transform.scale(game_background,(800,800))
game_background_rect=game_background_scale.get_rect()
game_background_rect.center=(screen_width/2,screen_height/2)

button_start=pygame.Rect(screen_width/2-100,screen_height/2-100,200,200)

while run:
    clock.tick(60)
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==ADD_BLOCK and not show_main_menu:
            random_x_value=random.randint(25,775)
            block=Block("pygame\\uhybanibloku\\image\\Block_of_Gold_JE6_BE3.png",25,random_x_value) #Vytvoření instance objektu blok
            all_block_list.add(block)
        if event.type==pygame.MOUSEBUTTONDOWN:
            if button_start.collidepoint(event.pos):
                show_main_menu=False

    if show_main_menu:
        screen.blit(game_background_scale,game_background_rect)
        pygame.draw.rect(screen,(255,0,0),button_start)

    if not show_main_menu:
        keys=pygame.key.get_pressed()


        all_block_list.update() #Update listu bloků
        player.update(keys) #Pohyb hráče
        player.draw(screen) #Vykreslení hráče
        all_block_list.draw(screen) #Vykrelsení všech bloků

        for block in all_block_list:
            if block.rect.top==795:
                score+=1
                print(score)
                score_text=score_font.render(f"Skore: {score}",True, (255,255,255))

        if pygame.sprite.spritecollide(player, all_block_list, False): #Kontrola kolize hráče s jakýmkoliv blokem z té group, False znamená, že ten blok při kolizi nezmizí (neudělá se self.kill())
            #Collide mask dělá to, že vezme ty dva bloky přes sebe a jediný s čím počíta jsou 0 a 1
            #Pokud to pozadí nemá barvu, tak se dá 0 při kolizi s lodí
            #Pokud se ale dotkne část bloku, která není transparentní, tak se to změní na 1 a 1 bude i u toho playera, což se nastaví na true
            pygame.time.delay(5000) #Hra se zastaví na pět vteřin
            run=False

        screen.blit(score_text,score_text_rect)
        
    pygame.display.update()

    pygame.time.delay(10)

pygame.quit()



