import arcade
from game.game import Game  # Импортируем класс Game из модуля game

def main():
    game = Game()
    game.setup()
    arcade.run()

if __name__ == "__main__":  # Проверка на основной модуль
    main()
