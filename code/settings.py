class Settings():
    """store all game settings"""
    def __init__(self):
        """"init game settings"""
        #screen
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_color =(0x71,0xc6,0x71)
        self.bg_color =(230,230,230)
        self.ship_speed_factor = 30
        self.ship_limit = 3

        self.bullet_speed_factor = 20
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 30

        self.alien_speed_factor = 2
        self.fleet_drop_speed = 100
        # move to right : 1 ; move to left :-1
        self.fleet_direction = 1

