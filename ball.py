import pygame
from pygame.sprite import Sprite


# todo Create the ball class


class Ball(Sprite):
    """Class to create the ball"""

    def __init__(self, pong):
        super().__init__()
        self.screen = pong.screen
        self.settings = pong.settings
        self.screen_rect = pong.screen_rect
        self.rect = pygame.rect.Rect(0, 0, 35, 23)
        self.rect.center = self.screen_rect.center
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def draw_ball(self):
        """Draws the ball unto the screen"""
        pygame.draw.circle(self.screen, self.settings.ball_color, self.rect.center, self.settings.ball_radius)

    def update(self):
        """Updates the current position of the ball"""
        self._move_around()
        if self.rect.top < self.screen_rect.top or self.rect.bottom > self.screen_rect.bottom:
            # change direction
            self.settings.reboundy *= -1

    def _move_around(self):
        """Moves the ball at a fixed rate"""
        self.y += (10 * self.settings.reboundy)
        self.rect.y = self.y
        self.x += 10 * self.settings.reboundx
        self.rect.x = self.x

