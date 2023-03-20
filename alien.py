import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """
    A class to represent a single alien in the fleet.
    """
    def __init__(self, screen, gameSetting):
        """
        Initialize the alien and set its starting position
        :param screen:
        :param gameSetting:
        """
        super().__init__()
        self.screen = screen

        self.settings = gameSetting

        # Load the image and set its rect attribute
        self.image = pygame.image.load('assets/image/nb_alien_ship.png')
        self.rect = self.image.get_rect()

        # Start each new alien hear the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = self.rect.x
        self.y = 100

    def blitme(self):
        """
        Draw the alien at its current location.
        :return:
        """
        self.screen.blit(self.img, self.rect)
