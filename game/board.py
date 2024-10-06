import arcade
from .pieces import Piece
from .settings import *

class Board:
    def __init__(self, width, height, cell_size, line_color=(128, 128, 128), line_width=2, sounds = None):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.line_color = line_color
        self.line_width = line_width
        self.board = [[0 for _ in range(width // cell_size)] for _ in range(height // cell_size)]
        self.current_piece = Piece()  # Начинаем с новой фигуры
        self.x = 0
        self.y = 0
        self.game_speed_timer = 0
        self.score = 0
        self.game_speed = 1
        self.sounds = sounds
        
    def check_full_rows(self):
        """Проверяет, есть ли заполненные строки, и удаляет их."""
        full_rows = []
        for i, row in enumerate(self.board):
            if all(row):
                full_rows.append(i)

        if full_rows:
            self.remove_full_rows(full_rows)
            self.update_score(len(full_rows))
            self.update_game_speed()
            

    def remove_full_rows(self, rows):
        """Удаляет заполненные строки и сдвигает остальные строки вниз."""
        for row in sorted(rows, reverse=True):
            del self.board[row]
            self.board.insert(0, [0 for _ in range(self.width // self.cell_size)])
    
    def update_score(self, num_rows):
        """Обновляет счет игрока в соответствии с количеством удаленных строк."""
        self.score += num_rows * 10
    
    def update(self, delta_time):
        self.game_speed_timer += delta_time
        # Проверяем, достаточно ли времени прошло для следующего движения вниз
        if self.game_speed_timer >= 1 / (GAME_SPEED + self.game_speed):
            self.game_speed_timer = 0
            # Логика обновления игрового поля (движение вниз, проверка)
            if not self.can_move(self.current_piece.shape, (1, 0)):
                # Если не можем двигаться вниз, фиксируем фигуру
                self.lock_piece()
                self.check_full_rows()
                self.current_piece = Piece()  # Генерируем новую фигуру
            else:
                self.current_piece.position[0] += 1
            

    def update_game_speed(self):
        """Увеличивает скорость игры в зависимости от количества очков."""
        self.game_speed = max(1, self.score // 5 + 1)

    def can_move(self, shape, offset):
        # Проверяем, может ли фигура сместиться в указанном направлении
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell:
                    x = self.current_piece.position[0] + offset[0] + i
                    y = self.current_piece.position[1] + offset[1] + j

                    if x < 0 or x >= len(self.board) or y < 0 or y >= len(self.board[0]) or self.board[x][y]:
                        return False
        return True


    def lock_piece(self):
        for i, row in enumerate(self.current_piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    x = self.current_piece.position[0] + i
                    y = self.current_piece.position[1] + j
                    if x >= 0 and x < len(self.board) and y >= 0 and y < len(self.board[0]):
                        self.board[x][y] = 1  # Фиксируем фигуру на игровом поле
        self.check_full_rows()
        self.current_piece = None
                        
