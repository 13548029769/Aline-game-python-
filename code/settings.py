class Settings():
    """store all game settings"""
    def __init__(self):
        """"init game settings"""
        #screen
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_color =(0x71,0xc6,0x71)
        self.bg_color =(230,230,230)

        self.ship_limit = 3

        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 30

        self.fleet_drop_speed = 5
        self.speedup_scale = 1.6
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        self.alien_speed_factor = 0.5
        self.ship_speed_factor = 0.5
        self.bullet_speed_factor = 2
        self.alien_point = 50
        self.bullet_width = 10

        # move to right : 1 ; move to left :-1
        self.fleet_direction = 1

    def increase_speed(self):
        """increase speed"""
        self.alien_speed_factor  *= self.speedup_scale
        self.ship_speed_factor   *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_point = int(self.speedup_scale * self.alien_point)
        self.bullet_width *= self.speedup_scale