import pygame
import game_function as fg
from settings import Settings
from ship import Ship
from game_stats import GameStats
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard


def run_game():
    """start game"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Aline invasion")
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    play_button = Button(ai_settings,screen,"PLAY")
    stats = GameStats(ai_settings)
    fg.create_feelt(ai_settings,screen,ship,aliens)
    sb = Scoreboard(screen,ai_settings,stats)


    #start
    while True:
        fg.check_events(ai_settings,screen,stats,play_button,ship,bullets,aliens,sb  )
        if stats.game_active:
            ship.update()
            fg.update_bullets(ai_settings,screen,ship,aliens,bullets,stats,sb)
            fg.update_alien(ai_settings,stats,screen,ship,aliens,bullets)

        fg.update_screen(ai_settings, screen, stats, ship, aliens, bullets,play_button,sb)

run_game()