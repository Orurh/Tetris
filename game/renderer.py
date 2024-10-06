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
                x, y = self._get_cell_position(j, i)
                arcade.draw_rectangle_outline(
                    x,
                    y,
                    self.board.cell_size,
                    self.board.cell_size,
                    self.board.line_color,
                    self.board.line_width,
                )

        # Рисуем занятые ячейки
        for i, row in enumerate(self.board.board):
            for j, cell in enumerate(row):
                if cell:
                    x, y = self._get_cell_position(j, i)
                    arcade.draw_rectangle_filled(
                        x,
                        y,
                        self.board.cell_size,
                        self.board.cell_size,
                        arcade.color.YELLOW,
                    )

    def draw_piece(self):
        piece = self.board.current_piece
        for i, row in enumerate(piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    x, y = self._get_piece_position(piece.position[1], piece.position[0], j, i)
                    arcade.draw_rectangle_filled(
                        x,
                        y,
                        self.board.cell_size,
                        self.board.cell_size,
                        arcade.color.RED
                    )

    def _get_cell_position(self, column, row):
        x = column * self.board.cell_size + self.board.x + self.board.cell_size // 2
        y = (self.board.height - row * self.board.cell_size) - self.board.cell_size + self.board.y + self.board.cell_size // 2
        return x, y

    def _get_piece_position(self, piece_column, piece_row, cell_column, cell_row):
        x = piece_column * self.board.cell_size + cell_column * self.board.cell_size + self.board.x + self.board.cell_size // 2
        y = self.board.height - (piece_row * self.board.cell_size + cell_row * self.board.cell_size) - self.board.cell_size + self.board.y + self.board.cell_size // 2
        return x, y
