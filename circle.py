import pygame
pygame.init()
screen= pygame.display.set_mode([500,500])
class Circle():
    def __init__(self,color,position,radius):
        self.c= color
        self.p= position
        self.r= radius
        self.s= screen
    def draw(self):
        pygame.draw.circle(self.s, self.c, self.p, self.r)
    def draw_c(self,a):
        self.r+= a
        pygame.draw.circle(self.s, self.c, self.p, self.r)

circle_1= Circle("white", (250,250), 100)
circle_2= Circle("purple",(250,250), 50)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type== pygame.MOUSEBUTTONDOWN:
            screen.fill("light blue")
            circle_1.draw()
            circle_2.draw()
            pygame.display.update()
        elif event.type== pygame.MOUSEBUTTONUP:
            screen.fill("light blue")
            circle_1.draw_c(10)
            circle_2.draw_c(10)
            pygame.display.update()
        elif event.type== pygame.MOUSEMOTION:
            pos= pygame.mouse.get_pos()
            circle_3= Circle("light green", pos, 10)
            circle_3.draw()
            pygame.display.update()