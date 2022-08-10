import pygame
import random
import math
# # import random
pygame.init()
s = pygame.display.set_mode((600, 600))
r = True

background=pygame.image.load('74.jpg')
playerImg = pygame.image.load('car.png')

playerx=300
playery=500
playerx_c=0
playery_c=0
# enamyimg = []
# enamyX = []
# enamyY = []
enamyY_change = 0.2
num_of_enamies = 2
enamyimg=pygame.image.load('car1.png')
enamyX=random.randint(0, 530)
enamyY=random.randint(-20, 50)
def enamy(x, y):
    s.blit(enamyimg, (x, y))
def player(x,y):
    s.blit(playerImg,(x,y))
def iscollesion(enamyX, enamyY,playerx, playery):
    distance = math.sqrt((math.pow(enamyX-playerx, 2)) +
                         (math.pow(enamyY-playery, 2)))
    if distance < 40:
        return True
    else:
        return False

while r:
    s.fill((0, 0, 0))
    s.blit(background,(0,0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            r = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                playerx_c=-1
            if i.key == pygame.K_RIGHT:
                playerx_c=1
            if i.key == pygame.K_UP:
                playery_c=-1
            if i.key == pygame.K_DOWN:
                playery_c=1
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT or i.key == pygame.K_UP or i.key == pygame.K_DOWN:
                playerx_c = 0
                playery_c = 0 
    if enamyY >= 600:
        enamyX=random.randint(0, 530)
        enamyY = random.randint(0, 50)
    collession = iscollesion(enamyX, enamyY, playerx,playery)
    if collession:
        enamyX=random.randint(0, 530)
        enamyY = random.randint(0, 50)
        


    playerx+=playerx_c
    if playerx <= 0:
        playerx = 0
    elif playerx >= 530:
        playerx = 530
    playery+=playery_c
    if playery >=530:
        playery = 530
    elif playery <=0:
        playery = 0
     
    player(playerx,playery)
    enamyY+=enamyY_change
    for i in range(num_of_enamies):
        enamy(enamyX, enamyY)
    pygame.display.update()
