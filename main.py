"""
@Description :
In Alien Invasion, the player controls a ship that appears at
the bottom center of the screen. The player can move the ship
right and left using the arrow keys and shoot bullets using the
spacer. When the game begins, a fleet of aliens fills the sky
and moves across and down the screen. The player shoots and
destroys the aliens. If the player shoots all the aliens, a new fleet
appears that moves faster than the previous fleet. If any alien hits
the player’s ship or reaches the bottom of the screen, the player
loses a ship. If the player loses three ships, the game ends.
"""

import sys
import pygame
from setting import Settings
from ship import Ship
import gameFunctions as gf
from alien import Alien
from pygame.sprite import Group


def run_game():
    """
    Initialize game and create a screen object
    :return:
    """
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screenWidth, game_settings.screenHeight)
    )
    ship = Ship(screen, game_settings)
    pygame.display.set_caption('Alien Invasion')

    while True: # start the game loop
        # check for events or inputs
        gf.checkEvents(game_settings, screen, ship, ship.bulletLst)
        ship.update()
        ship.bulletLst.update()
        gf.update_bullet_lst(ship.bulletLst)
        gf.updateScreen(game_settings, screen, ship, ship.bulletLst)


run_game()