import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, path,y,x=None):
        super().__init__()
        if x is None:
            x=0
        self.image=pygame.image.load(path) #Předá path jako argument té metody init
        self.image_scale=pygame.transform.scale(self.image,(100,100))
        self.rect=self.image_scale.get_rect()
        self.rect.center=(x,y)
    def update(self):
        self.rect.y+=1 #Při každém update toho spritu to zvýší souřadnici y o 1
    def draw(self, screen):
        screen.blit(self.image_scale,self.rect) #Vykreslí daný sprite objekt na obrazovku
    