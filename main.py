# import the necessary modules

import sys
from time import sleep

import pygame

from ball import Ball
from game_stats import GameStats
from paddle import LeftPaddle, RightPaddle
from scoreboard import ScoreBoard
from settings import Settings


class Pong:
    """Pong Game class"""

    def __init__(self):
        """Initialise the components of the game"""
        # initialize pygame
        pygame.init()

        # screen components
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption('Pong')
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings(self)
        self._create_components()
        # game stats
        self.stats = GameStats(self)
        # scoreboard
        self.sb = ScoreBoard(self)

    def run_game(self):
        """Main loop of the game"""
        while True:
            if bool(self.settings.game_active % 2):
                # if game is not paused
                self._check_events()
                self._detect_collisions()
                self._update_screen()
                pygame.mouse.set_visible(False)
                sleep(self.settings.sleep)
            else:
                # paused game
                self._check_events()

    def _check_events(self):
        """Checks for any form of activity with the keyboard or mouse"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._key_down_events(event)
            elif event.type == pygame.KEYUP:
                self._key_up_events(event)

    def _key_down_events(self, event):
        """Captures the events of a key pressed """
        if event.key == pygame.K_ESCAPE:
            sys.exit()

        # Right Paddle controls
        elif event.key == pygame.K_UP:
            self.right_paddle.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.right_paddle.moving_down = True

        # Left Paddle controls
        elif event.key == pygame.K_w:
            self.left_paddle.moving_up = True
        elif event.key == pygame.K_s:
            self.left_paddle.moving_down = True

        # space bar to pause
        elif event.key == pygame.K_SPACE:
            self.settings.game_active += 1

    def _key_up_events(self, event):
        """Captures the events of a key released"""
        # Right Paddle controls
        if event.key == pygame.K_DOWN:
            self.right_paddle.moving_down = False
        elif event.key == pygame.K_UP:
            self.right_paddle.moving_up = False

        # Left Paddle controls
        elif event.key == pygame.K_w:
            self.left_paddle.moving_up = False
        elif event.key == pygame.K_s:
            self.left_paddle.moving_down = False

    def _create_components(self):
        # left_paddle components
        self.left_paddle = LeftPaddle(self)
        # right paddle components
        self.right_paddle = RightPaddle(self)
        # ball component
        self.ball = Ball(self)
        # groups
        self.Balls = pygame.sprite.Group(self.ball)
        self.Paddles = pygame.sprite.Group(self.left_paddle, self.right_paddle)
        self.ball.draw_ball()

    def _update_screen(self):
        """Updates the screen with a new scenery"""
        self.screen.fill(self.settings.screen_bg_color)
        pygame.draw.line(surface=self.screen,
                         color=self.settings.screen_line_color,
                         start_pos=self.settings.screen_midbottom,
                         end_pos=self.settings.screen_midtop,
                         width=self.settings.screen_line_width)
        self.left_paddle.draw_paddle()
        self.right_paddle.draw_paddle()
        self.ball.draw_ball()
        self.ball.update()
        if self.ball.rect.left < self.screen_rect.left:
            self._reset_game()
            self.stats.right_score += 1
        elif self.ball.rect.right > self.screen_rect.right:
            self._reset_game()
            self.stats.left_score += 1
        self.sb.show_score()
        pygame.display.flip()

    def _detect_collisions(self):
        """Detects collision between ball and paddle"""
        collision = pygame.sprite.groupcollide(self.Balls, self.Paddles, False, False)
        if collision:
            self.settings.reboundx *= -1
            self.settings.sleep *= 0.9

    def _reset_game(self):
        """Resets all the components of the game back to their original positions"""
        self._create_components()
        self.settings.sleep = 0.07

if __name__ == '__main__':
    pong = Pong()
    pong.run_game()
