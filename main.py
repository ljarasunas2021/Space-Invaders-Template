import pygame
import random
from engine import Engine
from engine.object import Object
from engine.text import Text
from engine.audio import Audio

engine = Engine()

# create the screen
screen = engine.createScreen(800, 600)

# Title and Icon
engine.setName("Space Invaders")

# Background
background = Object('images/background.png', 0, 0)

# Music
Audio('audio/background.wav', True, 0.25)

# Initialize score
score = 0

# Player
player = Object('images/spaceship.png', 368, 500)
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

# create enemies
for i in range(rowsOfEnemies):
    for j in range(columnsOfEnemies):
        enemy = Object('images/ufo.png', currentEnemyXPos, currentEnemyYPos)
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
bulletSpeed = 20


# Create bullet and add to array
def fireBullet():
    bullet = Object('images/bullet.png', player.posX + 16, player.posY - 16)
    bullets.append(bullet)
    Audio('audio/laser.wav', False, 0.25)


# Game Loop
running = True
while running:
    for event in engine.getEvents():
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

    # Apply the movement and check for boundaries
    atLeftBoundary = False
    atRightBoundary = False

    for enemy in enemies:
        enemy.posX += enemyXChange
        enemy.posY += enemyYChange

        if enemy.posX <= 0:
            atLeftBoundary = True
        elif enemy.posX >= 736:
            atRightBoundary = True

    for enemy in enemies:
        if atLeftBoundary:
            enemyXChange = enemyXSpeed
            enemy.posY += enemyYSpeed
        elif atRightBoundary:
            enemyXChange = -enemyXSpeed
            enemy.posY += enemyYSpeed

    # Move bullets and check collisions
    for bullet in bullets:
        bullet.posY -= bulletSpeed
        for enemy in enemies:
            if bullet.checkCollision(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                Audio('audio/explosion.wav', False, 0.25)
                score += 1

    # Background
    background.render(screen)

    # Display player
    player.render(screen)

    # Display enemy
    for enemy in enemies:
        enemy.render(screen)

    # render bullets
    for bullet in bullets:
        bullet.render(screen)

    scoreText = Text("Score: " + str(score), 10, 10)
    scoreText.render(screen)

    # update display
    engine.updateDisplay()
