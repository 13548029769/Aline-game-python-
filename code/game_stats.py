import json
class GameStats():
    """Track game statistics"""
    def __init__(self,ai_settings):
        """init the statistics"""
        self.ai_settings = ai_settings
        self.game_active = False
        self.load_game_data_from_file()
        self.rest_stats()
        self.high_score = self.game_data["high_score"]

    def rest_stats(self):
        """initialization Likely to change variable at game running time"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1


    def load_game_data_from_file(self):
        with open("game_data/game_data.json","r") as game_data_file:
            self.game_data = json.load(game_data_file)



    def dump_game_date_to_file(self,high_score):
        self.game_data["high_score"] = high_score
        with open("game_data/game_data.json","w") as game_data_file:
            self.game_data = json.dump(self.game_data,game_data_file)


