import pygame
import game_function as fg
from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
    """start game"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Aline invasion")
    ship = Ship(ai_settings,screen)
    bullets = Group()

    #start
    while True:
        fg.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        fg.update_screen(ai_settings,screen,ship,bullets)


run_game()