import pygame


#define snail

class Snail(pygame.sprite.Sprite):
  
  def __init__(self, height, width):
    super().__init__()

    self.image = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
    self.rect = self.image.get_rect(midbottom = (600, 300))
snail_alive = True
snail_respawn_timer = 60
snail_lives = 3
