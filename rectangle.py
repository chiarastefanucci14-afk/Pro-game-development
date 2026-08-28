import pygame
pygame.init()
screen= pygame.display.set_mode([500,500])
class rect():
    def __init__(self,rect_color,x,y,w,h):
        self.c= rect_color
        self.x= x
        self.y= y
        self.w= w
        self.h= h
        self.s= screen
    def draw(self):
        pygame.draw.rect(self.s, self.c, (self.x, self.y, self.w, self.h))
    def draw_r(self,a):
        self.h+= a
        self.w+= a
        pygame.draw.rect(self.s, self.c, (self.x, self.y, self.w, self.h))

rect_1= rect("white", 250,250,100, 100)
rect_2= rect("purple",250,250,50, 50)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type== pygame.MOUSEBUTTONDOWN:
            screen.fill("light blue")
            rect_1.draw()
            rect_2.draw()
            pygame.display.update()
        elif event.type== pygame.MOUSEBUTTONUP:
            screen.fill("light blue")
            rect_1.draw_r(10)
            rect_2.draw_r(10)
            pygame.display.update()
        elif event.type== pygame.MOUSEMOTION:
            pos= pygame.mouse.get_pos()
            rect_3= rect("light green", pos[0], pos[1],10, 10)
            rect_3.draw()
            pygame.display.update()