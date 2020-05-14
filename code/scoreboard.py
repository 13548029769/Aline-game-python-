import pygame.font

class Scoreboard():
    def __init__(self,screen,ai_settings,stats):
        """initialize scoreboard attribute"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # setting scoreboard font
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        self.prep_score()


    def prep_score(self):
        round_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)


        # show score at up right corner of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """show score on screen"""
        self.screen.blit(self.score_image,self.score_rect)