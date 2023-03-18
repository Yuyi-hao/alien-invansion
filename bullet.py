import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    A class to manage bullets fired from the ship
    """
    def __init__(self, game_settings, screen, ship):
        super().__init__()
        self.screen = screen 

        self.rect = pygame.Rect(0, 0, game_settings.bulletWidth, game_settings.bulletHeight)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = game_settings.bulletColor
        self.speedFactor = game_settings.bulletSpeedFactor
    
    def update(self):
        """
        Move the bullet up the screen 
        """
        self.y -= self.speedFactor
        self.rect.y = self.y
    
    def drawBullet(self):
        """
        Draw the bullet to the screen 
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
    