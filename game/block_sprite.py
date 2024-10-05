import arcade

class BlockSprite(arcade.Sprite):
    def __init__(self, size):
        super().__init__()
        self.width = size
        self.height = size
        self.color = arcade.color.WHITE
        self.texture = arcade.load_texture(":resources\\images\\box.png/home/orurh/Документы/VSCode/Tetris/env/lib/python3.12/site-packages/arcade/resources/images/topdown_tanks/tank_green.png")
        

    def draw(self):
        arcade.draw_texture_rectangle(self.center_x, self.center_y, self.width, self.height, self.texture)
