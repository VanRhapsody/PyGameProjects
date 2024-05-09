import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, path,x,y,speed):
        super().__init__()
        self.image=pygame.image.load(path) #Předá path jako argument té metody init
        self.image_scale=pygame.transform.scale(self.image,(100,100))
        self.rect=self.image_scale.get_rect()
        self.rect.center=(x,y)
        self.speed=speed
    def move(self,keys): #argument je pygame.keys.get_pressed
        if keys[pygame.K_d]:
            if self.rect.x<750:
                self.rect.x+=self.speed
        if keys[pygame.K_a]:
            if self.rect.x>0:
                self.rect.x-=self.speed
    def draw(self, screen):
        screen.blit(self.image_scale,self.rect) #Vykreslí daný sprite objekt na obrazovku