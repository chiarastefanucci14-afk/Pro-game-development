import pygame
import time
import random
pygame.init()
screen= pygame.display.set_mode([600,600])
bee= pygame.image.load("Images\\bee.png")
flower= pygame.image.load("Images\\flower.png")
grass= pygame.image.load("Images\\grass.jpg")
score= 0
font= pygame.font.SysFont("Times New Roman", 50)
bee_rect = bee.get_rect()
bee_rect.x = 300
bee_rect.y = 300
velocity= 1
W=600
H=600

flower_rect = flower.get_rect()
flower_rect.x = 100
flower_rect.y = 100
def draw(score):
    score_text= font.render("Score: "+ str(score),1,"midnight blue")
    screen.blit(score_text,(210,20))
def bumble(keys_pressed,bee):
        if keys_pressed[pygame.K_LEFT]and bee.x-velocity:
            bee.x-= velocity
        if keys_pressed[pygame.K_RIGHT]and bee.x+velocity+bee.width<W:
            bee.x+= velocity
        if keys_pressed[pygame.K_UP]and bee.y-velocity>0:
            bee.y-= velocity
        if keys_pressed[pygame.K_DOWN]and bee.y+velocity+bee.height<H-15:
            bee.y+= velocity
        

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    screen.blit(grass,(0,0))
    screen.blit(flower,(flower_rect.x, flower_rect.y))
    screen.blit(bee,(bee_rect.x, bee_rect.y))   
    keys_pressed=pygame.key.get_pressed()
    bumble(keys_pressed,bee_rect)    
    if abs(bee_rect.x-flower_rect.x)<30 and abs(bee_rect.y-flower_rect.y)<30:
        flower_rect.x=random.randint(90,510)
        flower_rect.y=random.randint(90,510)
        score+= 1
    draw(score)
    pygame.display.update()
