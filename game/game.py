import arcade
from .board import Board
from .renderer import Renderer
import time
from .settings import *

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_GREY)
        

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.board = Board(BOARD_WIDTH, BOARD_HEIGHT, BOARD_CELL_SIZE)
        self.renderer = Renderer(self.board)
        self.speed = GAME_SPEED
        
    
    def on_draw(self):
        arcade.start_render()
        self.renderer.draw_board()
        self.renderer.draw_piece()



    def on_update(self, delta_time):
        self.board.update(delta_time)
        self.renderer.draw_board()
        self.renderer.draw_piece()
        time.sleep(0.0)
        
    def on_key_press(self, key, modifiers):
        
        if key == arcade.key.LEFT:  # Движение влево
            if self.board.can_move(self.board.current_piece.shape, (0, -1)):
                self.board.current_piece.position[1] -= 1
        elif key == arcade.key.RIGHT:  # Движение вправо
            if self.board.can_move(self.board.current_piece.shape, (0, 1)):
                self.board.current_piece.position[1] += 1
        elif key == arcade.key.DOWN:  # движение вниз
            if self.board.can_move(self.board.current_piece.shape, (1, 0)):
                self.board.current_piece.position[0] += 1
        elif key == arcade.key.UP:  # Вращение
            # Запоминаем старую форму фигуры
            old_shape = self.board.current_piece.shape
            # Поворачиваем фигуру
            self.board.current_piece.rotate()
            # Проверяем, можем ли мы разместить фигуру в новом положении
            if not self.board.can_move(self.board.current_piece.shape, (0, 0)):
                # Если нет, возвращаем старую форму фигуры
                self.board.current_piece.shape = old_shape

