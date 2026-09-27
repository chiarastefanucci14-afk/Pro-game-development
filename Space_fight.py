import pygame
pygame.init()
W= 600
H= 600
screen= pygame.display.set_mode((W,H))
pygame.display.set_caption("Space Fight!")
boarder= pygame.Rect(W//2-5,0,10,H)
font= pygame.font.SysFont("Times New Roman", 50)
fps=60
velocity= 1
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
def draw(red,yellow,red_health,yellow_health,red_bullets,yellow_bullets):
    screen.blit(space,(0,0))
    pygame.draw.rect(screen,"black",boarder)
    red_health_text= font.render("health: "+ str(red_health),1,"white")
    yellow_health_text= font.render("health: "+ str(yellow_health),1,"white")
    screen.blit(red_health_text,(W-red_health_text.get_width()-10,10))
    screen.blit(yellow_health_text,(10,10))
    screen.blit(yellow_ss,(yellow.x, yellow.y))
    screen.blit(red_ss,(red.x, red.y))
    for i in red_bullets:
        pygame.draw.rect(screen,"red",i)
    for i in yellow_bullets:
        pygame.draw.rect(screen,"yellow",i)
    pygame.display.update()
def bullets(yellow_bullets,red_bullets,yellow,red):
    for i in yellow_bullets:
        i.x+=bullet_speed
        if red.colliderect(i):
            pygame.event.post(pygame.event.Event(red_hit))
            yellow_bullets.remove(i)
        elif i.x> W:
            yellow_bullets.remove(i)
    for i in red_bullets:
        i.x-=bullet_speed
        if yellow.colliderect(i):
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullets.remove(i)
        elif i.x> W:
            red_bullets.remove(i)
def red_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT]and red.x-velocity>boarder.x+boarder.width:
        red.x-= velocity
    if keys_pressed[pygame.K_RIGHT]and red.x+velocity+red.width<W:
        red.x+= velocity
    if keys_pressed[pygame.K_UP]and red.y-velocity>0:
        red.y-= velocity
    if keys_pressed[pygame.K_DOWN]and red.y+velocity+red.height<H-15:
        red.y+= velocity
def yellow_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a]and yellow.x-velocity>0:
        yellow.x-= velocity
    if keys_pressed[pygame.K_d]and yellow.x+velocity+yellow.width<boarder.x:
        yellow.x+= velocity
    if keys_pressed[pygame.K_w]and yellow.y-velocity>0:
        yellow.y-= velocity
    if keys_pressed[pygame.K_s]and yellow.y+velocity+yellow.height<H-15:
        yellow.y+= velocity
red= pygame.Rect(400,200,ssw,ssh)
yellow= pygame.Rect(150,200,ssw,ssh)
red_health=10
yellow_health=10
yellow_bullets=[]
red_bullets=[]
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
    draw(red,yellow,red_health,yellow_health,red_bullets,yellow_bullets)
    keys_pressed=pygame.key.get_pressed()
    red_movement(keys_pressed,red)
    yellow_movement(keys_pressed,yellow)
    bullets(yellow_bullets,red_bullets,yellow,red)
