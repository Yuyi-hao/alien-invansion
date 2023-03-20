import sys
import pygame
from bullet import Bullet
from alien import Alien


def checkEvents(gameSettings, screen, ship, bullets):
    """
    Respond to key presses and mouse events.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeyDownEvent(event, gameSettings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            checkKeyUpEvent(event, ship)


def checkKeyUpEvent(event, ship):
    """
    Handle key Release events
    """
    if event.key == pygame.K_RIGHT:
        ship.motionR = False
    if event.key == pygame.K_LEFT:
        ship.motionL = False
    if event.key == pygame.K_SPACE:
        ship.fire = False

def checkKeyDownEvent(event, gameSettings, screen, ship, bullets):
    """
    Handle key Press events. 
    """
    if event.key == pygame.K_RIGHT:
        ship.motionR = True
    if event.key == pygame.K_LEFT:
        ship.motionL = True
    if event.key == pygame.K_SPACE:
        ship.fire = True
    elif event.key == pygame.K_q:
        sys.exit()
        #  Create a new bullet and add it to bullet group
        # newBullet = Bullet(gameSettings, screen, ship)
        # bullets.add(newBullet)


def updateScreen(gameSettings, screen, ship, aliens, bullets):
    """
    Update images on screen and flip to the new screen,
    """
    screen.fill(gameSettings.bgColor)
    for bullet in bullets.sprites():
        bullet.drawBullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullet_lst(bullets):
    """
    Update bullet list and remove bullets that can't be displayed on screen
    :param bullets:
    :return:
    """
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_fleet(game_settings, screen, aliens):
    """ Create a full fleet of aliens."""
    alien = Alien(screen, game_settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    available_space_H = game_settings.screenWidth - 2*alien_width
    available_space_V = game_settings.screenHeight - 2*alien_height

    number_alien_x = available_space_H // (2*alien_width) + 1
    number_alien_y = available_space_V // (2*alien_height) + 1

    for j in range(number_alien_y-1):
        for i in range(number_alien_x):
            alien = Alien(screen, game_settings)
            alien.x = alien_width + 2*alien_width * i
            alien.y = alien_height + 2*alien_height * j
            alien.rect.x = alien.x
            alien.rect.y = alien.y
            aliens.add(alien)
