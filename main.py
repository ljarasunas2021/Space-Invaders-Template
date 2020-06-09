import pygame
import random
from engine import Engine
from engine.object import Object
from engine.text import Text
from engine.audio import Audio


def moveLeft():
    global player, PLAYERXSPEED

    player.pos_x -= PLAYERXSPEED * engine.delta_time
    if player.pos_x < 0:
        player.pos_x = 0


def moveRight():
    global player, PLAYERXSPEED

    player.pos_x += PLAYERXSPEED * engine.delta_time
    if player.pos_x >= 736:
        player.pos_x = 736


def activate_can_shoot():
    global can_shoot
    can_shoot = True


# Create bullet and add to array
def fire_bullet():
    global can_shoot

    if can_shoot:
        bullet = Object(engine, 'images/bullet.png',
                        player.pos_x + 16, player.pos_y - 16)
        bullets.append(bullet)

        laser_sound.play()

        can_shoot = False
        engine.add_timer(TIMEBETWEENSHOTS, activate_can_shoot)


engine = Engine()

# create the screen
screen = engine.create_screen(800, 600)

# Title and Icon
engine.set_name("Space Invaders")

# Background
engine.set_background(engine, 'images/background.png', screen)

# Set Audio
background_music = Audio('audio/background.wav', True, 0.25)
background_music.play()
laser_sound = Audio('audio/laser.wav', False, 0.25)
explosion_sound = Audio('audio/explosion.wav', False, 0.25)

# Initialize score
score = 0
score_text = Text(engine, "Score: " + str(score), 10, 10)

# Initialize game over text
game_over_text = Text(engine, "Game Over", 200, 250, 64)
game_over_text.hide()

good_job_text = Text(engine, "Good Job", 225, 250, 64)
good_job_text.hide()

# Player
player = Object(engine, 'images/spaceship.png', 368, 500)
PLAYERXSPEED = 200

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
        enemy = Object(engine, 'images/ufo.png', current_enemy_x_pos,
                       current_enemy_y_pos)
        enemies.append(enemy)

        current_enemy_x_pos += enemy.width + XDISTANCEBETWEENENEMIES

    current_enemy_y_pos += enemy.height + YDISTANCEBETWEENENEMIES
    current_enemy_x_pos = STARTINGENEMYXPOS

ENEMYXSPEED = 200
enemy_dir = 1
ENEMYYSPEED = 400

# Initialize bullet array
bullets = []
BULLETSPEED = 600
can_shoot = True
TIMEBETWEENSHOTS = 0.5

engine.on_key_down(pygame.K_LEFT, moveLeft)
engine.on_key_down(pygame.K_a, moveLeft)
engine.on_key_down(pygame.K_RIGHT, moveRight)
engine.on_key_down(pygame.K_d, moveRight)
engine.on_key_pressed(pygame.K_SPACE, fire_bullet)


def update():
    global enemies, bullets, enemy_dir, score, game_over_text

    # Apply the movement and check for boundaries
    at_left_boundary = False
    at_right_boundary = False

    for enemy in enemies:
        enemy.pos_x += enemy_dir * ENEMYXSPEED * engine.delta_time

        if enemy.pos_x <= 0:
            at_left_boundary = True
        elif enemy.pos_x >= 736:
            at_right_boundary = True

    for enemy in enemies:
        if at_left_boundary:
            enemy_dir = 1
            enemy.pos_y += ENEMYYSPEED * engine.delta_time
        elif at_right_boundary:
            enemy_dir = -1
            enemy.pos_y += ENEMYYSPEED * engine.delta_time

    # Move bullets and check collisions
    for bullet in bullets:
        bullet.pos_y -= BULLETSPEED * engine.delta_time
        for enemy in enemies:
            if bullet.check_collision(enemy):
                bullet.destroy()
                bullets.remove(bullet)
                enemy.destroy()
                enemies.remove(enemy)
                explosion_sound.play()
                score += 1
                if len(enemies) == 0:
                    good_job_text.show()

    # Render score text
    score_text.change_text("Score: " + str(score))

    # Check for Game Over
    for enemy in enemies:
        if player.check_collision(enemy):
            game_over_text.show()
            for enemy in enemies:
                enemy.destroy()
            enemies = []


engine.start(update)
