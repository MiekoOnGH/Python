import pygame

class Ship():

    def __init__(self, screen):

        self.screen = screen

        self.image = pygame.image.load('images/ship1_small.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.speed = 1

    def update(self):
        if self.moving_right:
            self.rect.x += self.speed
        elif self.moving_left:
            self.rect.x -= self.speed
        elif self.moving_up:
            self.rect.y -= self.speed
        elif self.moving_down:
            self.rect.y += self.speed

    def blitme(self):

        self.screen.blit(self.image, self.rect)