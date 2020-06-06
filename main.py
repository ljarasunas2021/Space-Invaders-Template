import pygame
import random
from object import object

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = object('images/background.png', 0, 0, screen)

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/spaceship.png')
pygame.display.set_icon(icon)

score = 0

# Player
player = object('images/spaceship.png', 368, 500, screen)
playerXChange = 0
playerXSpeed = 10

# Enemy
enemies = []
columnsOfEnemies = 4
rowsOfEnemies = 2
startingEnemyXPos = 100
startingEnemyYPos = 100
xDistanceBetweenEnemies = 50
yDistanceBetweenEnemies = 40
currentEnemyXPos = startingEnemyXPos
currentEnemyYPos = startingEnemyYPos

for i in range(rowsOfEnemies):
    for i in range(columnsOfEnemies):
        enemy = object('images/ufo.png', currentEnemyXPos,
                       currentEnemyYPos, screen)
        enemies.append(enemy)
        currentEnemyXPos += enemy.width + xDistanceBetweenEnemies

    currentEnemyYPos += enemy.height + yDistanceBetweenEnemies
    currentEnemyXPos = startingEnemyXPos

enemyXSpeed = 10
enemyXChange = enemyXSpeed
enemyYSpeed = 10
enemyYChange = 0

# Initialize bullet array
bullets = []
bulletSpeed = 10


# Create bullet and add to array
def fireBullet():
    bullet = object('images/bullet.png', player.posX +
                    16, player.posY - 16, screen)
    bullets.append(bullet)


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        # Check if window should close
        if event.type == pygame.QUIT:
            running = False

        # Movement if key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerXChange = -playerXSpeed
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerXChange = playerXSpeed
            if event.key == pygame.K_SPACE:
                fireBullet()
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and playerXChange < 0:
                playerXChange = 0
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and playerXChange > 0:
                playerXChange = 0

                # Apply the movement
    player.posX += playerXChange

    # Set Boundaries to player position
    if player.posX <= 0:
        player.posX = 0
    elif player.posX >= 736:
        player.posX = 736

    newEnemyXChange = enemyXChange
    newEnemyYChange = 0

    # Apply the movement and check for boundaries
    for enemy in enemies:
        enemy.posX += enemyXChange
        enemy.posY += enemyYChange

        if enemy.posX <= 0:
            newEnemyXChange = enemyXSpeed
            newEnemyYChange = enemyYSpeed
        elif enemy.posX > 736:
            newEnemyXChange = -enemyXSpeed
            newEnemyYChange = enemyYSpeed

    # Set boundaries
    for enemy in enemies:
        enemyXChange = newEnemyXChange
        enemy.posY += newEnemyYChange

        # Move bullets and check collisions
    for bullet in bullets:
        bullet.posY -= bulletSpeed
        for enemy in enemies:
            if bullet.checkCollision(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1

    # Background
    background.render()

    # Display player
    player.render()

    # Display enemy
    for enemy in enemies:
        enemy.render()

    # render bullets
    for bullet in bullets:
        bullet.render()

    # update display
    pygame.display.update()
