import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        #load ship and get rect
        self.image = pygame.image.load('images/rocket.bmp') #load images
        self.rect = self.image.get_rect() #'rect' makes a rectangle around image
        self.screen_rect = screen.get_rect() #screen's rect

        #starts each new ship at the bottom

        #self.rect is ship,     self.screen_rect is the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #store a decimal for he ship's center
        self.center = float(self.rect.centerx)

        #movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        #updates center value NOT rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor

    def blitme(self): #draws the image
        self.screen.blit(self.image, self.rect)