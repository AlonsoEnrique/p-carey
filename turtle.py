import arcade


class Turtle:
    def __init__(self):
        # TODO: assign random name for display to user
        self.name = ''
        # km/h
        self.speed = 1

    @property
    def body(self):
        arcade.draw_circle_outline(100, 200, 16, arcade.color.AIR_FORCE_BLUE, 1)

    def movement(self):
        raise NotImplementedError

    def on_draw(self):
        self.body
