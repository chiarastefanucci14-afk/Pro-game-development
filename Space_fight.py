import pygame
pygame.init()
W= 600
H= 600
screen= pygame.display.set_mode((W,H))
pygame.display.set_caption("Space Fight!")
boarder= pygame.Rect(W//2-5,0,10,H)
font= pygame.font.SysFont("Times New Roman", 50)
fps=60
speed= 5
bullet_speed= 7
max_bullets= 3
yellow_hit= pygame.USEREVENT+1
red_hit= pygame.USEREVENT+2
ssw=55
ssh=40
yellow_image= pygame.image.load("Images\\yellow.png")
yellow_ss= pygame.transform.rotate(pygame.transform.scale(yellow_image,(ssw,ssh)),90)
red_image= pygame.image.load("Images\\red.png")
red_ss= pygame.transform.rotate(pygame.transform.scale(red_image,(ssw,ssh)),270)
space= pygame.transform.scale(pygame.image.load("Images\\space#2.png"),(W,H))
def draw(red,yellow):
    screen.blit(space,(0,0))
    pygame.draw.rect(screen,"black",boarder)
    screen.blit(yellow_ss,(yellow.x, yellow.y))
    screen.blit(red_ss,(red.x, red.y))
    pygame.display.update()
red= pygame.Rect(400,400,ssw,ssh)
yellow= pygame.Rect(100,400,ssw,ssh)
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
    draw(red,yellow)