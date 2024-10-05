import arcade
from .settings import *

class Renderer:
    def __init__(self, board):
        self.board = board

    def draw_board(self):
        """
        Рисует игровое поле.
        """
        # Рисуем сетку игрового поля
        for i in range(self.board.height // self.board.cell_size):
            for j in range(self.board.width // self.board.cell_size):
                x = j * self.board.cell_size + self.board.x
                y = i * self.board.cell_size + self.board.y
                arcade.draw_rectangle_outline(
                    x + self.board.cell_size // 2,
                    y + self.board.cell_size // 2,
                    self.board.cell_size,
                    self.board.cell_size,
                    self.board.line_color,
                    self.board.line_width,
                )

        # Рисуем занятые ячейки
        for i, row in enumerate(self.board.board):
            for j, cell in enumerate(row):
                if cell:
                    x = j * self.board.cell_size + self.board.x
                    y = (self.board.height - i * self.board.cell_size) - self.board.cell_size + self.board.y
                    arcade.draw_rectangle_filled(
                        x + self.board.cell_size // 2,
                        y + self.board.cell_size // 2,
                        self.board.cell_size,
                        self.board.cell_size,
                        arcade.color.YELLOW,
                    )


    def draw_piece(self):
        piece = self.board.current_piece
        for i, row in enumerate(piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    x = piece.position[1] * self.board.cell_size + j * self.board.cell_size + self.board.x
                    y = self.board.height - (piece.position[0] * self.board.cell_size + i * self.board.cell_size) - self.board.cell_size + self.board.y
                    arcade.draw_rectangle_filled(
                        x + self.board.cell_size // 2,
                        y + self.board.cell_size // 2,
                        self.board.cell_size,
                        self.board.cell_size,
                        arcade.color.RED
                    )