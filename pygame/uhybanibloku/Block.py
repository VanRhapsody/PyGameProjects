"""import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, path, y,x=None):
        super().__init__()
        if x is None:
            x=0
        self.image=pygame.image.load(path).convert_alpha() #Předá path jako argument té metody init
        self.image_scale=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image_scale.get_rect()
        self.rect.center=(x,y)
    def update(self):
        self.rect.y+=1 #Při každém update toho spritu to zvýší souřadnici y o 1
        if self.rect.top > 600: #Když je blok níže než 600, odstraní ho to
            self.kill()
    def draw(self, screen):
        screen.blit(self.image_scale,self.rect) #Vykreslí daný sprite objekt na obrazovku"""


import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, path, y, x=None):
        super().__init__()
        if x is None:
            x = 0
        self.original_image = pygame.image.load(path).convert_alpha()  #Předá path jako argument té metody init
        self.image = pygame.transform.scale(self.original_image, (100,100))  # Scale the image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y += 5 #Při každém update toho spritu to zvýší souřadnici y o 1
        if self.rect.top >= 800: #Když je blok níže než 600, odstraní ho to  
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)  #Vykreslí daný sprite objekt na obrazovku