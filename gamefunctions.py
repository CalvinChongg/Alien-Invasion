import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    #closes the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #responds to keypresses
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        
#if key is pressed it will move
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


#if released it stops
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


#updates the screen
def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #redraws all bullets behind the ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #updates the screen
    pygame.display.flip()