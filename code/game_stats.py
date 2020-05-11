class GameStats():
    """Track game statistics"""
    def __init__(self,ai_settings):
        """init the statistics"""
        self.ai_settings = ai_settings
        self.game_active = False
        self.rest_stats()


    def rest_stats(self):
        """initialization Likely to change variable at game running time"""
        self.ships_left = self.ai_settings.ship_limit