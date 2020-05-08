import sys
import pygame
from bullet import Bullet

def check_events(ai_settings,screen,ship,bullets):
    """respond keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship,bullets)

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """respond keyboard"""
    if event.key == pygame.K_RIGHT:
        ship.moveing_right = True
    elif event.key == pygame.K_LEFT:
        ship.moveing_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
        bullets.sprites().burst = True



def check_keyup_events(event,ship,bullets):
    """respond keyboard"""
    if event.key == pygame.K_RIGHT:
        ship.moveing_right = False
    elif event.key == pygame.K_LEFT:
        ship.moveing_left = False
    elif event.key == pygame.K_SPACE:
        bullets.sprites().burst = False


def update_screen(ai_settings,screen,ship,bullets):
    """update screen image, flush the screen"""
    screen.fill(ai_settings.bg_color)

    # draw all bullets after spacecraft and aline
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    pygame.display.flip()