import pygame



# define Explosion

class Explosion(pygame.sprite.Sprite):
  
  def __init__(self, height, width):
    super().__init__()
    
    self.image = pygame.image.load('graphics/download.jpg').convert_alpha()
    self.rect = self.image.get_rect(center = (80,225))

  