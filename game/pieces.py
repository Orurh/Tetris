import random
import arcade

SHAPES = [
    [[1, 1, 1, 1]],# I
    [[1, 1],[1, 1]],  # O
    
    [[0, 1, 1],[1, 1, 0]],  # S
    
    [[1, 1, 0],[0, 1, 1]],  # Z
    
    [[1, 0, 0],[1, 1, 1]],  # L
    
    [[0, 0, 1],[1, 1, 1]],  # J
    
    [[0, 1, 0],[1, 1, 1]],  # T
]

class Piece:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.position = [0, 4]  # Начальная позиция (ряд, колонка)

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])] # Поворот фигуры
