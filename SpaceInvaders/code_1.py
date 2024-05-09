import pygame

pygame.init()

screen_width=1000
screen_height=800

screen=pygame.display.set_mode((screen_width,screen_height))

class Crab(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image=self.get_image()
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
    def draw(self):
        image_resized=self.get_image()
        screen.blit(image_resized,self.crab)
    def get_image(self):
        image=pygame.image.load("SpaceInvaders/images/crab.png")
        image_resized=pygame.transform.scale(image,(100,100))
        return image_resized
    def move_left(self):
        self.rect.centerx+=step
    def move_right(self):
        self.rect.centerx-=step
    def move_down(self):
        self.rect.centery+=step
    
class Squid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image=self.get_image()
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
    def draw(self):
        image_resized=self.get_image()
        screen.blit(image_resized,self.squid)
    def get_image(self):
        image=pygame.image.load("SpaceInvaders/images/squid.png")
        image_resized=pygame.transform.scale(image,(100,100))
        return image_resized
    def move_left(self):
        self.rect.centerx+=step
    def move_right(self):
        self.rect.centerx-=step
    def move_down(self):
        self.rect.centery+=step
    
class Octopus(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image=self.get_image()
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
    def draw(self):
        image_resized=self.get_image()
        screen.blit(image_resized,self.octopus)
    def get_image(self):
        image=pygame.image.load("SpaceInvaders/images/octopus.png")
        image_resized=pygame.transform.scale(image,(100,100))
        return image_resized
    def move_left(self):
        self.rect.centerx+=step
    def move_right(self):
        self.rect.centerx-=step
    def move_down(self):
        self.rect.centery+=step

    
class UFO(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image=self.get_image()
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
    def draw(self):
        image_resized=self.get_image()
        screen.blit(image_resized,self.UFO)
    def get_image(self):
        image=pygame.image.load("SpaceInvaders/images/ufo.png")
        image_resized=pygame.transform.scale(image,(100,100))
        return image_resized
    def move_left(self):
        self.rect.centerx+=step
    def move_right(self):
        self.rect.centerx-=step
    def move_down(self):
        self.rect.centery+=step


step=100
padding=50

clock=pygame.time.Clock()

octopus1=Octopus(0,100)
octopus2=Octopus(step,100)
octopus3=Octopus(step*2,100)
octopus4=Octopus(step*3,100)

squid1=Squid(0,100+step)
squid2=Squid(step,100+step)
squid3=Squid(step*2,100+step)
squid4=Squid(step*3,100+step)

crab1=Crab(0,100+step*2)
crab2=Crab(step,100+step*2)
crab3=Crab(step*2,100+step*2)
crab4=Crab(step*3,100+step*2)

ufo1=UFO(0,100+step*3)
ufo2=UFO(step,100+step*3)
ufo3=UFO(step*2,100+step*3)
ufo4=UFO(step*3,100+step*3)

enemies=pygame.sprite.Group()

enemies.add(octopus1, octopus2, octopus3, octopus4, squid1, squid2, squid3, squid4, crab1, crab2, crab3, crab4, ufo1, ufo2, ufo3, ufo4)

counter=0


run=True

left=False

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    screen.fill((0,0,0))

    enemies.update()
    
    enemies.draw(screen)

    if octopus1.rect.x == 0 or octopus4.rect.x==step*9:
        octopus1.move_down()
        octopus2.move_down()
        octopus3.move_down()
        octopus4.move_down()
        squid1.move_down()
        squid2.move_down()
        squid3.move_down()
        squid4.move_down()
        crab1.move_down()
        crab2.move_down()
        crab3.move_down()
        crab4.move_down()
        ufo1.move_down()
        ufo2.move_down()
        ufo3.move_down()
        ufo4.move_down()
        print("yes")
        if octopus1.rect.x==step:
            left=False
        elif octopus4.rect.x==step*9:
            left=True

    if counter%100==0:
        if left:
            octopus1.move_left()
            octopus2.move_left()
            octopus3.move_left()
            octopus4.move_left()
            squid1.move_left()
            squid2.move_left()
            squid3.move_left()
            squid4.move_left()
            crab1.move_left()
            crab2.move_left()
            crab3.move_left()
            crab4.move_left()
            ufo1.move_left()
            ufo2.move_left()
            ufo3.move_left()
            ufo4.move_left()
        else:
            octopus1.move_right()
            octopus2.move_right()
            octopus3.move_right()
            octopus4.move_right()
            squid1.move_right()
            squid2.move_right()
            squid3.move_right()
            squid4.move_right()
            crab1.move_right()
            crab2.move_right()
            crab3.move_right()
            crab4.move_right()
            ufo1.move_right()
            ufo2.move_right()
            ufo3.move_right()
            ufo4.move_right()

    


    

    counter+=1

    clock.tick(60)

    pygame.display.update()

pygame.quit()