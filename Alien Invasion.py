import sys
import pygame
from settings import Settings
from ship import Ship
import gamefunctions as gf
from pygame.sprite import Group

def run_game():
    # makes a screen, with settings class
    pygame.init() #starts
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)) #screen size according to settings class
    pygame.display.set_caption("Alien Invasion") #screen name

    #make a ship
    ship = Ship(ai_settings, screen)
    
    #makes a group to store Bullets
    bullets = Group()





    #Main Game Loop
    while True:
        #looks for keyboard and mouse inputs
        gf.check_events(ai_settings, screen, ship, bullets)
        #movement updates
        ship.update()
        bullets.update()
        #redraws the screen
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()