import arcade

from conf import SCREEN_WIDTH, SCREEN_HEIGHT
from turtle import Turtle


class CareyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, title="Carey the game")
        self.turtle = None

    def setup(self):
        self.turtle = Turtle()

    def on_draw(self):
        arcade.start_render()

        self.turtle.on_draw()


def main():
    window = CareyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
