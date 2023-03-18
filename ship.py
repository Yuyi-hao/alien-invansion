import pygame
from bullet import Bullet
from pygame.sprite import Group


class Ship:
    """
    Initialize the ship and set its starting positions.
    """
    def __init__(self, screen, shipSetting):
        self.screen = screen
        self.shipSetting = shipSetting
        self.image = pygame.image.load('assets/image/nb_space_ship.png')
        self.rect = self.image.get_rect()
        self.screenRect = self.screen.get_rect()

        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom
        self.center = float(self.rect.centerx)
        self.bulletLst = Group()
        self.motionL = False
        self.motionR = False
        self.fire = False
        self.allowedBullet = 5

    def blitme(self):
        """
        Draw the ship at its current location.
        """
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """
        Update the ship's position based on the movement flag.
        """
        if self.motionL and self.rect.left > 0:
            self.rect.centerx -= self.shipSetting.speedFactor
        if self.motionR and self.rect.right < self.screenRect.right:
            self.rect.centerx += self.shipSetting.speedFactor
        if self.fire and len(self.bulletLst) <= self.allowedBullet:
            newBullet = Bullet(self.shipSetting, self.screen, self)
            self.bulletLst.add(newBullet)
        
        # self.rect.centerx = self.center