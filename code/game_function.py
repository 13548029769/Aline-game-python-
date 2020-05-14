import sys
import pygame
from bullet import Bullet
from alien import Aline
from random import randint
from time import sleep


def check_events(ai_settings,screen,stats,play_button,ship,bullets,aliens):
    """respond keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            """respond the button and mouse events"""
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(mouse_x, mouse_y, play_button, stats,aliens,bullets,ai_settings,ship,screen)


def check_play_button(mouse_x, mouse_y, play_button, stats,aliens,bullets,ai_settings,ship,screen):
    """star game when user click the play button"""
    if play_button.rect.collidepoint(mouse_x, mouse_y) and \
            not stats.game_active:
        ai_settings.initialize_dynamic_settings()

        # Hide cursor
        # pygame.mouse.set_visible(False)

        #reset game statistics
        stats.rest_stats()
        stats.game_active = True

        aliens.empty()
        bullets.empty()

        create_feelt(ai_settings, screen, ship, aliens)
        ship.center_ship()




def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """respond keyboard"""
    if event.key == pygame.K_RIGHT:
        ship.moveing_right = True
    elif event.key == pygame.K_LEFT:
        ship.moveing_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)


def check_keyup_events(event,ship):
    """respond keyboard"""
    if event.key == pygame.K_RIGHT:
        ship.moveing_right = False
    elif event.key == pygame.K_LEFT:
        ship.moveing_left = False
    # elif event.key == pygame.K_SPACE:
    #     bullets.sprites().burst = False


def update_screen(ai_settings, screen, stats, ship, aliens, bullets,play_button,sb):
    """update screen image, flush the screen"""
    screen.fill(ai_settings.bg_color)
    sb.show_score()

    # draw all bullets after spacecraft and aline
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def update_bullets(ai_settings,screen,ship,aliens,bullets,stats,sb):
    """update bullets position, and free outside screen's bullet object memory"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(aliens, bullets, screen, ship, ai_settings, stats,sb)


def check_bullet_alien_collisions(aliens, bullets, screen, ship, ai_settings,stats,sb):
    # Detect whether the bullet hits the alien. If it hits the alien,
    # make the bullet and the alien disappear
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collision:
        for aliens in collision.values():
            stats.score += ai_settings.alien_point * len(aliens)
            sb.prep_score()

    if len(aliens) == 0:
        # delete all bullets
        bullets.empty()
        ai_settings.increase_speed()
        # create aliens
        create_feelt(ai_settings, screen, ship, aliens)



def fire_bullets(ai_settings,screen,ship,bullets):
    """spacecraft fire"""
    # create new bullet object add into bullets group
    if len(bullets) <= ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        # bullets.sprites().burst = True


def create_feelt(ai_settings,screen,ship,aliens):
    """create alien fleet"""
    alien = Aline(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    # creat alien fleet on screen
    for row_number in range(number_rows):
        # create a row of aliens
        for alien_number in range(number_aliens_x):
            # create an alien add into current row
            create_aline(ai_settings, screen, aliens, alien_number, row_number)


def create_aline(ai_settings,screen,aliens,alien_number,row_number):
    """calculate how many aliens can be contained in each line"""
    random_num1 = randint(0,8)
    alien = Aline(ai_settings,screen)
    alien_width = alien.rect.width
    # alien.x = alien_width + 2 * alien_width * alien_number
    alien.x = alien_width + 2 * alien_width * random_num1
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_aliens_x(ai_settings,alien_width):
    """calculate how many aliens can be contained in each line"""
    available_space_x = ai_settings.screen_width -  2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x


def get_number_rows(ai_settings,ship_height,alien_height):
    """calculate how many aliens can be contained in each line"""
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def update_alien(ai_settings,stats,screen,ship,aliens,bullets):
    """update all aliens position"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)

    check_alien_bottom(ai_settings, stats, screen, ship, aliens, bullets)

    for alien in aliens.copy():
        if alien.rect.top <= 0:
            aliens.remove(alien)


def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    """respond hit between alien and ship"""
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_feelt(ai_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(1)
    else:
        stats.game_active = False
        # pygame.mouse.set_visible(True)


def check_fleet_edges(ai_settings,aliens):
    """operate of aliens at edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings,aliens):
    """move down aliens and change their direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_alien_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    """check if aliens is at the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break