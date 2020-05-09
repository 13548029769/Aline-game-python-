import pygame

from pygame.sprite import Sprite

class Aline(Sprite):
    """a class representative aline"""
    def __init__(self,ai_settings,screen):
        """init aline setting and initialization"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #loading alien image and setting its attribute
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # setting alien accurate position
        self.x = float(self.rect.x)

    def blitme(self):
        """draw alien at specific position"""
        self.screen.blit(self.image,self.rect)


    def update(self):
        """move right and left aliens"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x


    def check_edges(self):
        """if alien at the edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True