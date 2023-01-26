import pygame


#define snail

class Fireball(pygame.sprite.Sprite):
  
  def __init__(self, height, width):
    super().__init__()

    self.image = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
    self.rect = self.image.get_rect(midbottom = (600, 300))
homing_timer = 600