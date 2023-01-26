import pygame



# define Player

class Player(pygame.sprite.Sprite):
  
  def __init__(self, height, width):
    super().__init__()
    
    self.image = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
    self.rect = self.image.get_rect(center = (80,225))

player_alive = True
























