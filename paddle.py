import pygame
from pygame.sprite import Sprite


# todo Create left_paddle class


class Paddle(Sprite):

    def __init__(self, pong=None):
        """Initialize the properties of a left_paddle"""
        super().__init__()
        self.screen = pong.screen
        self.screen_rect = pong.screen_rect
        self.settings = pong.settings
        self.rect = pygame.Rect(0, 0, self.settings.paddle_wight, self.settings.paddle_height)
        self.color = None
        self.y = float(self.rect.y)
        self.moving_up = False
        self.moving_down = False

    def move_up(self):
        """Moves the left_paddle up with a constant speed"""
        self.y -= self.settings.paddle_speed
        self.rect.y = self.y

    def move_down(self):
        """Moves the left_paddle down with a constant speed"""
        self.y += self.settings.paddle_speed
        self.rect.y = self.y

    def draw_paddle(self):
        """Draws the left_paddle on the screen"""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.move_up()
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.move_down()
        pygame.draw.rect(self.screen, self.color, self.rect)


class LeftPaddle(Paddle):
    """Inherits from the paddle class to create the left paddle"""

    def __init__(self, *args):
        """Initialize the features of the left paddle"""
        pong = args[0]
        super().__init__(pong=pong)
        self.rect.midleft = pong.screen_rect.midleft
        self.y = float(self.rect.y)
        self.color = self.settings.paddle_color


class RightPaddle(Paddle):
    """Inherits from the paddle class to create the right paddle"""

    def __init__(self, *args):
        """Initialize the features of the left paddle"""
        pong = args[0]
        super().__init__(pong=pong)
        self.rect.midright = pong.screen_rect.midright
        self.y = float(self.rect.y)
        self.color = self.settings.paddle_color
