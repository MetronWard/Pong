class Settings:
    """Contains all the variables and constants for the game"""

    def __init__(self, pong):
        # game
        self.sleep = 0.07
        self.game_active = 1
        # screen settings
        self.screen = pong.screen
        self.screen_bg_color = (0, 0, 0)
        self.screen_line_color = (225, 225, 225)
        self.screen_line_width = 3
        self.screen_rect = self.screen.get_rect()
        self.screen_midtop = self.screen_rect.midtop
        self.screen_midbottom = self.screen_rect.midbottom
        # paddle settings
        self.paddle_wight = 14
        self.paddle_height = 100
        self.paddle_speed = 10
        self.paddle_color = (225, 225, 225)
        # ball settings
        self.ball_color = (225, 225, 225)
        self.ball_radius = 15.0
        self.reboundy = -1
        self.reboundx = -1
        # scoreboard settings
        self.font_size = 50
        self.text_color = (225, 225, 225)
