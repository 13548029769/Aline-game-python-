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

        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)