import arcade

from conf import SCREEN_WIDTH, SCREEN_HEIGHT


class CareyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, title="Carey the game")


def main():
    window = CareyGame()
    # window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
