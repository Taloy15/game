import pygame
import os
import math
from random import randint
import sys

# Import
from movement import *
from class_snail import *
from class_player import *
from explosion import *
from class_fireball import *
from pygame.locals import QUIT

pygame.init()

# Zet basisvariabelen
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('skill issue')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)


#sprites group
enemy_sprites_list = pygame.sprite.Group()
player_sprites_group = pygame.sprite.Group()
boomboom = pygame.sprite.Group()


# Importeer dingen
sky_surface = pygame.image.load('graphics/sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()
text_surface = test_font.render('we are gaming', 'true', 'blue')



#create entitys

SnailEnemy1 = Snail(20, 20)
SnailEnemy1.rect.x = 600
SnailEnemy1.rect.y = 265

enemy_sprites_list.add(SnailEnemy1)

Player1 = Player(40, 20)
Player1.rect.x = 80
Player1.rect.y = 220

player_sprites_group.add(Player1)

Eksplosie = Explosion(40, 20)
Eksplosie.rect.x = Player1.rect.x
Eksplosie.rect.y = Player1.rect.y

key_pressed = pygame.key.get_pressed()

boomboom.add(Eksplosie)

Fireball1 = Fireball(20, 20)
Fireball1.rect.x = 600
Fireball1.rect.y = 265

enemy_sprites_list.add(Fireball1)

#movement dingen
running = True

while running:
    for event in pygame.event.get():

#maakt het mogelijk om de game uit te zetten
        if event.type == pygame.QUIT:
            running = False

        if pygame.key.get_pressed()[pygame.K_a]:
            move_left = True
        else:
            move_left = False
        if pygame.key.get_pressed()[pygame.K_d]:
            move_right = True
        else:
            move_right = False

          
#Zorgt ervoor dat de player reageert op Keyboard inputs
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                in_the_air = True
            elif event.key == pygame.K_w:
                in_the_air = True

#up_down_movement
    if in_the_air:
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMP_VELOCITY:
            in_the_air = False
            Y_VELOCITY = JUMP_VELOCITY
        Player1.rect.y -= Y_VELOCITY

      
#left_right_movement
    if move_left and not move_right:
        if X_VELOCITY < 10:
            X_VELOCITY += 0.3
        else:
            X_VELOCITY = 10
        Player1.rect.x -= X_VELOCITY
    elif move_right and not move_left:
        if X_VELOCITY < 10:
            X_VELOCITY += 0.3
        else:
            X_VELOCITY = 10
        Player1.rect.x += X_VELOCITY
    else:
        X_VELOCITY = BASE_X_VELOCITY

      
#snail shit
    SnailEnemy1.rect.x -= 1
    if abs(Player1.rect.x - Fireball1.rect.x) < 500:
      if SnailEnemy1.rect.right <= 0:
        SnailEnemy1.rect.x = 800

    
      if Fireball1.rect.x < Player1.rect.x:
        Fireball1.rect.x += 2 
      else:
        Fireball1.rect.x -= 2
      if Fireball1.rect.y < Player1.rect.y:
        Fireball1.rect.y += 2 
      else:
        Fireball1.rect.y -= 2 

      
# Add background scenery
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (350, 100))

  
    # Draw them fuckers
    enemy_sprites_list.draw(screen)
    player_sprites_group.draw(screen)

    #collide with map

    #  if Player1.self.bottom.colliderect()

    # collide with enemies
    if snail_alive:
      if Player1.rect.colliderect(
        SnailEnemy1.rect) and in_the_air and player_alive:
        pygame.sprite.Sprite.kill(SnailEnemy1)
        snail_alive = False
    elif snail_lives > 0:
      snail_respawn_timer -= 1
      if snail_respawn_timer == 0:
        snail_alive = True
        snail_lives -= 1
        enemy_sprites_list.add(SnailEnemy1)
        SnailEnemy1.rect.x = 600
        SnailEnemy1.rect.y = 265
    if Player1.rect.colliderect(
      SnailEnemy1.rect) and not in_the_air and snail_alive:
      pygame.sprite.Sprite.kill(Player1)
      player_alive = False
    if Player1.rect.colliderect(
      Fireball1.rect) and player_alive:
      pygame.sprite.Sprite.kill(Player1)
    homing_timer -= 1
    if homing_timer == 0:
      pygame.sprite.Sprite.kill(Fireball1)
      Fireball1.rect.x = 100000
      Fireball1.rect.y = 100000
    pygame.display.update()
    clock.tick(60)

pygame.quit()
