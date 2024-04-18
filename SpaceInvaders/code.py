import pygame

pygame.init()

screen_width=1000
screen_height=800

screen=pygame.display.set_mode((screen_width,screen_height))

class Crab:
    def __init__(self, x, y):
        self.crab=self.get_image().get_rect()
        self.crab.center=(x,y)
    def draw(self):
        image_resized=self.get_image()
        screen.blit(image_resized,self.crab)
    def get_image(self):
        image=pygame.image.load("SpaceInvaders/images/crab.png")
        image_resized=pygame.transform.scale(image,(100,100))
        return image_resized


crab1=Crab(screen_width//2,600)
crab2=Crab(screen_width//2+100,600)

run=True

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
    crab1.draw()
    crab2.draw()

    pygame.display.update()

pygame.quit()