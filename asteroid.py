import pygame
import random
pygame.init()
screen= pygame.display.set_mode((600,600))
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Images\\Asteroid.jpg")
        self.image=pygame.transform.scale(self.image,(100,100))
        self.rect= self.image.get_rect()
        self.rect.x=random.randint(0,500)
        self.rect.y=random.randint(0,500)
player_group= pygame.sprite.Group()
for i in range (5):
    player_group.add(Asteroid())
space= pygame.image.load("Images\\Space.png")
while True:
    for i in pygame.event.get():
        if i.type== pygame.QUIT:
            pygame.quit()
    screen.blit(space, (0,0))
    player_group.draw(screen)
    pygame.display.update()
    
