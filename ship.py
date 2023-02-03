import pygame

class Ship:
    """
    Initialize the ship and set its starting positions.
    """
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('assets/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screenRect = self.screen.get_rect()

        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom

    def blitme(self):
        """
        Draw the ship at its current location.
        """
        self.screen.blit(self.image, self.rect)