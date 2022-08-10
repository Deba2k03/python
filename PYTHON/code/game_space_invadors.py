import pygame
import random
import math

from pygame import mixer

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))
# 600-height   800-width

# title
pygame.display.set_caption("Space invadors")
# load image
icon = pygame.image.load('rocket.png')
#
pygame.display.set_icon(icon)

# background
background = pygame.image.load('background.jpg')

# background sound
mixer.music.load('background.wav')
mixer.music.play(-1)
# player
playerimg = pygame.image.load('player.png')

# place the image in axis with the help of pixel
playerX = 370  # width
playerY = 480  # height
playerX_change = 0


# enamy
enamyimg = []
enamyX = []
enamyY = []
enamyX_change = []
enamyY_change = []
num_of_enamies = 5

for i in range(num_of_enamies):
    enamyimg.append(pygame.image.load('enamy.png'))
    # place the image in axis with the help of pixel
    # enamyX=370  #width
    enamyX.append(random.randint(0, 736))
    # enamyY=50 #height
    enamyY.append(random.randint(50, 150))
    enamyX_change.append(2)
    enamyY_change.append(10)

# bullet
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 3
# ready=you can't see the bullet in the screen
# fire state=the bullet is corrently moving
bullet_state = "ready"


# score

score_value = 0
# for more types of font https://www.dafont.com/
font = pygame.font.Font('CoffeeExtra.ttf', 32)

testX = 10
testY = 10

# game over text
game_font = pygame.font.Font('CoffeeExtra.ttf', 64)

# score


def show_score(p, q):
    score = font.render("Score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (p, q))

# game over func


def game_over_text():
    over = game_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over, (200, 250))


# player func
def player(x, y):
    screen.blit(playerimg, (x, y))

# enamy func


def enamy(x, y, i):
    screen.blit(enamyimg[i], (x, y))

# bullet func


def fire_bullet(a, b):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (a+16, b+10))


def iscollesion(enamyX, enamyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enamyX-bulletX, 2)) +
                         (math.pow(enamyY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# game loop
running = True
while running:

    # change color
    # R G B =red green blue inside the fill
    # https://www.rapidtables.com/convert/color/hex-to-rgb.html
    screen.fill((0, 0, 0))

    # background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check wheather its right or left
        if event.type == pygame.KEYDOWN:
            # print("a keystroke is pressed")
            if event.key == pygame.K_LEFT:
                # print("left arrow is pressed")
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                # print("right arrow key is pressed")
                playerX_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    # get the current x co_ordinates of the space-ship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print("keystroke has been realesed")
                playerX_change = 0

    # call the method  (player method)
    # playerY-=0.1

    # 5+ -0.3 =5-0.3
    # 5+0.3
    playerX += playerX_change
    # checking for boundary of a spaceship does not go out of bounds
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    # enamy movement
    for i in range(num_of_enamies):

        # game over
        if enamyY[i] > 300:
            for j in range(num_of_enamies):
                enamyY[j] = 1000
            game_over_text()
            break
        enamyX[i] += enamyX_change[i]
        if enamyX[i] <= 0:
            enamyX_change[i] = +0.3
            enamyY[i] += enamyY_change[i]
        elif enamyX[i] >= 736:
            enamyX_change[i] = -0.3
            enamyY[i] += enamyY_change[i]
        # collession
        collession = iscollesion(enamyX[i], enamyY[i], bulletX, bulletY)
        if collession:
            collession_sound = mixer.Sound('explosion.wav')
            collession_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            # after collession create new enamy
            enamyX[i] = random.randint(0, 736)
            enamyY[i] = random.randint(50, 150)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)

    show_score(testX, testY)

    for i in range(num_of_enamies):
        enamy(enamyX[i], enamyY[i], i)
    pygame.display.update()
