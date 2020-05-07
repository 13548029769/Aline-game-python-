import pygame

class Ship():
    def __init__(self,screen):
        """init and set spacecraft position"""
        self.screen = screen

        """loading spacecraft picture and acquire exterior rectangle"""
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        """init spacecraft at bottom center of screen"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image,self.rect)