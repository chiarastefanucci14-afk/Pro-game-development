import pygame
from pygame.locals import *
pygame.init()
clock= pygame.time.Clock()
fps= 60
W= 864
H= 936
screen= pygame.display.set_mode((W,H))
pygame.display.set_caption("FLAPY BIRD!")
ground_scroll= 0
scroll_speed= 4
backround= pygame.image.load("Images\\Backround- Flapy bird.png")
ground= pygame.image.load("Images\\Ground- Flapy bird.png")
class Flapy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images= []
        self.index= 0
        self.counter= 0
        for i in range(1,4):
            img= pygame.image.load(f"Images\\Bird {i}.png")
            self.images.append(img)
while True:
    clock.tick(fps)
    screen.blit(backround,(0,0))
    screen.blit(ground,(ground_scroll,768))
    ground_scroll-= scroll_speed
    if abs(ground_scroll)> 35:
        ground_scroll=0
    for i in pygame.event.get():
        if i.type== pygame.QUIT:
            pygame.quit()
    pygame.display.update()
