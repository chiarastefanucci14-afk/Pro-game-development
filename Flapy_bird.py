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
flying= False
game_over= False
pipe_gap= 150
pipe_frequency= 1500
last_pipe= pygame.time.get_ticks()-pipe_frequency
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
        self.image= self.images[self.index]
        self.rect= self.image.get_rect()
        self.rect.center= [x,y]
        self.velocity= 0
        self.click= False    
    def update(self):
        if flying== True:
            self.velocity+= 0.5
            if self.velocity>8:
                self.velocity= 8
            if self.rect.bottom<768:
                self.rect.y+= int(self.velocity)
        if game_over== False:
            if pygame.mouse.get_pressed()[0]==1 and self.click==False:
                self.click= True
                self.velocity=-10
            if pygame.mouse.get_pressed()[0]==0:
                self.click= False
            self.counter+=1
            flap_cool_down= 5
            if self.counter>flap_cool_down:
                self.counter= 0
                self.index+= 1
                if self.index>=len(self.images):
                    self.index= 0
            self.image= self.images[self.index]
            self.image= pygame.transform.rotate(self.images[self.index],self.velocity*-2)
        else:
            self.image= pygame.transform.rotate(self.images[self.index],-90)
class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,position):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("Images\\stick- Flapy bird.png")
Bird_group= pygame.sprite.Group()
flapy_bird= Flapy(100,int(H/2))
Bird_group.add(flapy_bird)
while True:
    clock.tick(fps)
    screen.blit(backround,(0,0))
    Bird_group.draw(screen)
    Bird_group.update()
    screen.blit(ground,(ground_scroll,768))
    if flapy_bird.rect.bottom> 768:
        game_over= True
        flying= False
    if game_over== False:
        ground_scroll-= scroll_speed
        if abs(ground_scroll)> 35:
            ground_scroll=0
    for i in pygame.event.get():
        if i.type== pygame.QUIT:
            pygame.quit()
        if i.type== pygame.MOUSEBUTTONDOWN and flying== False and game_over== False:
            flying= True
    pygame.display.update()
