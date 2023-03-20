
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

import pygame
from setting import Settings
from ship import Ship
import gameFunctions as game_func
from pygame.sprite import Group


def run_game():
    """
    Initialize game and create a screen object
    :return:
    """
    pygame.init()  # initialize
    game_settings = Settings()  # game settings
    screen = pygame.display.set_mode(
        (game_settings.screenWidth, game_settings.screenHeight)
    )
    pygame.display.set_caption(game_settings.game_title)
    ship = Ship(screen, game_settings)
    aliens = Group()
    game_func.create_fleet(game_settings, screen, aliens)

    while True:  # start the game loop
        # check for events or inputs
        game_func.checkEvents(game_settings, screen, ship, ship.bulletLst)
        ship.update()
        ship.bulletLst.update()
        game_func.update_bullet_lst(ship.bulletLst)
        game_func.updateScreen(game_settings, screen, ship, aliens, ship.bulletLst)

run_game()
