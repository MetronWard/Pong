import pygame.font


class ScoreBoard:
    """Creates the scoreboard for the game"""

    def __init__(self, pong):
        """Initialise the components of the scoreboard"""
        self.screen = pong.screen
        self.screen_rect = pong.screen_rect
        self.settings = pong.settings
        self.stats = pong.stats
        self.font = pygame.font.SysFont(None, self.settings.font_size)
        self.show_score()

    def show_score(self):
        """Displays the score onto the game screen"""
        self.score = (self.stats.left_score, self.stats.right_score)
        game_str = f"{self.score[0]} : {self.score[1]}"
        self.score_image = self.font.render(game_str, True, self.settings.text_color, self.settings.screen_bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.screen.blit(self.score_image, self.score_rect)
