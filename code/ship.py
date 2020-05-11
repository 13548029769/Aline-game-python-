import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        """init and set spacecraft position"""
        self.screen = screen
        self.ai_settings = ai_settings

        """loading spacecraft picture and acquire exterior rectangle"""
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        """init spacecraft at bottom center of screen"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        """store the min value in attribute 'centerx'"""
        self.center = float(self.rect.centerx)

        """spacecraft move flag"""
        self.moveing_right = False
        self.moveing_left = False


    def blitme(self):
        self.screen.blit(self.image,self.rect)


    def update(self):
        """modify spacecraft position accord to move flag"""
        if self.moveing_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moveing_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center


    def center_ship(self):
        """make spacecraft on center of screen"""
        self.center = self.screen_rect.centerx