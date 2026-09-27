import pygame
from pygame.locals import*
from time import*
pygame.init()
screen=pygame.display.set_mode ((600,600))
pygame.display.set_caption("Rocket game")
rocket= pygame.image.load("Images\\rocket.png")
space= pygame.image.load("Images\\Space.png")
rocketx= 300
rockety= 300
keys= [False,False,False,False,False]
while rockety< 600:
    screen.blit(space, (0,0))
    screen.blit(rocket, (rocketx, rockety))
    pygame.display.flip()
    
    for i in pygame.event.get():
        if i.type== pygame.QUIT:
            pygame.quit()
        if i.type==pygame.KEYDOWN:
            if i.key== K_UP:
                keys[0]= True
            if i.key== K_DOWN:
                keys[1]= True
            if i.key== K_RIGHT:
                keys[2]= True
            if i.key== K_LEFT:
                keys[3]= True
            if i.key== K_SPACE:
                keys[4]= True
           
        if i.type== pygame.KEYUP:
            if i.key== K_UP:
                keys[0]= False
            if i.key== K_DOWN:
                keys[1]= False
            if i.key== K_RIGHT:
                keys[2]= False
            if i.key== K_LEFT:
                keys[3]= False
            if i.key== K_SPACE:
                keys[4]= False
    if keys [0]:
        if rockety>0:
            rockety-= 1
        if rocketx<600:
            rocketx+= 1
    if keys [1]:
        if rockety<550:
            rockety+= 1
        if rocketx>0:
            rocketx-= 1
    if keys [2]:
        if rocketx<600:
            rocketx+= 1
        if rockety<550:
            rockety+= 1
    if keys [3]:
        if rocketx>0:
            rocketx-= 1
        if rockety>0:
            rockety-= 1
    if keys [4]: 
        rockety -=2
    rockety+= 0.3
print("Game over")