import pygame

class Ship:
    """A class to manage the ship."""

    #two parameters: self referene and reference to the current instance of the AlienInvasion class (gives ship access to
    # all AlienInvasion game resources)
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        #assign screen to instance of ship so all instances can access
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #places ships in correct screen location
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        #movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        #update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location(specified by self.rect)."""
        self.screen.blit(self.image, self.rect)