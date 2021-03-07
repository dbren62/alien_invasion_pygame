import pygame

class Ship:
    """A class to manage the ship."""

    #two parameters: self referene and reference to the current instance of the AlienInvasion class (gives ship access to
    # all AlienInvasion game resources)
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        #assign screen to instance of ship so all instances can access
        self.screen = ai_game.screen
        #places ships in correct screen location
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #movement flag
        self.moving_right = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """Draw the ship at its current location(specified by self.rect)."""
        self.screen.blit(self.image, self.rect)