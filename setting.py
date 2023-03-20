class Settings:
    """
    A class to store all the settings and global variable for Alien Invasion.
    """
    def __init__(self):
        # screen settings
        self.screenWidth = 800
        self.screenHeight = 600
        self.bgColor = (230, 230, 230)
        self.speedFactor = 1
        self.game_title = "Alien Invasion"

        # Bullet settings 
        self.bulletSpeedFactor = 1
        self.bulletWidth = 3
        self.bulletHeight = 15
        self.bulletColor = (60, 60, 60)
        