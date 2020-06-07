import pygame
import random
from engine import Engine
from engine.object import Object
from engine.text import Text
from engine.audio import Audio

engine = Engine()

# create the screen
screen = engine.create_screen(800, 600)

# Title and Icon
engine.set_name("Space Invaders")

# Background
background = Object('images/background.png', 0, 0)

# Set Audio
background_music = Audio('audio/background.wav', True, 0.25)
background_music.play()
laser_sound = Audio('audio/laser.wav', False, 0.25)
explosion_sound = Audio('audio/explosion.wav', False, 0.25)

# Initialize score
score = 0

# Initialize game over text
game_over_text = None

# Player
player = Object('images/spaceship.png', 368, 500)
player_x_change = 0
PLAYERXSPEED = 10

# Enemy
enemies = []
COLUMNSOFENEMIES = 4
ROWSOFENEMIES = 2
STARTINGENEMYXPOS = 100
STARTINGENEMYYPOS = 100
XDISTANCEBETWEENENEMIES = 50
YDISTANCEBETWEENENEMIES = 40
current_enemy_x_pos = STARTINGENEMYXPOS
current_enemy_y_pos = STARTINGENEMYYPOS

# create enemies
for i in range(ROWSOFENEMIES):
    for j in range(COLUMNSOFENEMIES):
        enemy = Object('images/ufo.png', current_enemy_x_pos,
                       current_enemy_y_pos)
        enemies.append(enemy)

        current_enemy_x_pos += enemy.width + XDISTANCEBETWEENENEMIES

    current_enemy_y_pos += enemy.height + YDISTANCEBETWEENENEMIES
    current_enemy_x_pos = STARTINGENEMYXPOS

ENEMYXSPEED = 10
enemy_x_change = ENEMYXSPEED
ENEMYYSPEED = 40
enemy_y_change = 0

# Initialize bullet array
bullets = []
BULLETSPEED = 20


# Create bullet and add to array
def fire_bullet():
    bullet = Object('images/bullet.png', player.pos_x + 16, player.pos_y - 16)
    bullets.append(bullet)
    laser_sound.play()


# Game Loop
running = True
while running:
    for event in engine.get_events():
        if event.type == pygame.QUIT:
            running = False

        # Movement if key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_x_change = -PLAYERXSPEED
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_x_change = PLAYERXSPEED

            if event.key == pygame.K_SPACE:
                fire_bullet()

        if event.type == pygame.KEYUP:

            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and player_x_change < 0:
                player_x_change = 0
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and player_x_change > 0:
                player_x_change = 0

    # Apply the movement
    player.pos_x += player_x_change

    # Set Boundaries to player position
    if player.pos_x <= 0:
        player.pos_x = 0
    elif player.pos_x >= 736:
        player.pos_x = 736

    # Apply the movement and check for boundaries
    at_left_boundary = False
    at_right_boundary = False

    for enemy in enemies:
        enemy.pos_x += enemy_x_change
        enemy.pos_y += enemy_y_change

        if enemy.pos_x <= 0:
            at_left_boundary = True
        elif enemy.pos_x >= 736:
            at_right_boundary = True

    for enemy in enemies:
        if at_left_boundary:
            enemy_x_change = ENEMYXSPEED
            enemy.pos_y += ENEMYYSPEED
        elif at_right_boundary:
            enemy_x_change = -ENEMYXSPEED
            enemy.pos_y += ENEMYYSPEED

    # Move bullets and check collisions
    for bullet in bullets:
        bullet.pos_y -= BULLETSPEED
        for enemy in enemies:
            if bullet.check_collision(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                explosion_sound.play()
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

    # Render score text
    score_text = Text("Score: " + str(score), 10, 10)
    score_text.render(screen)

    # Check for Game Over
    for enemy in enemies:
        if player.check_collision(enemy):
            game_over_text = Text("Game Over", 200, 250, 64)

    if game_over_text != None:
        game_over_text.render(screen)

    # update display
    engine.update_display()
