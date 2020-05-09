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
    aliens = Group()
    fg.create_feelt(ai_settings,screen,ship,aliens)


    #start
    while True:
        fg.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        fg.update_bullets(bullets)
        fg.update_alien(ai_settings,aliens)
        fg.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()