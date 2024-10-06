import arcade


class GameInfo:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.level = 1
        self.score = 0

    def update_level(self, game_speed):
        self.level = game_speed

    def update_score(self, score):
        self.score = score

    def draw(self):
        arcade.draw_text(f"Level: {self.level}", self.screen_width -
                         200, self.screen_height - 50, arcade.color.WHITE, 20)
        arcade.draw_text(f"Score: {self.score}", self.screen_width -
                         200, self.screen_height - 81, arcade.color.WHITE, 20)
