import pygame
pygame.init()
screen= pygame.display.set_mode((600,600))
class Rocket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Images\\rocket.png")
        self.rect= self.image.get_rect()
    def movement(self,keys):
        if keys[pygame.K_UP]:
            self.rect.y-= 2
        if keys[pygame.K_DOWN]:
            self.rect.y+= 2    
        if keys[pygame.K_RIGHT]:
            self.rect.x+= 2
        if keys[pygame.K_LEFT]:
            self.rect.x-= 2
player= Rocket()
player_group= pygame.sprite.Group()
player_group.add(player)
space= pygame.image.load("Images\\Space.png")
while True:
    for i in pygame.event.get():
        if i.type== pygame.QUIT:
            pygame.quit()
    keys= pygame.key.get_pressed()
    player.movement(keys)
    screen.blit(space, (0,0))
    player_group.draw(screen)
    pygame.display.update()
    

