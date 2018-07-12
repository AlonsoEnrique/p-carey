import arcade


class Turtle:
    """ Turtle

    speed: POSITIVE INTEGER
    body
    sound_when_swim

    """
    def __init__(self):
        # TODO: assign random name for display to user
        self.name = ''
        self.x_position = 30
        self.y_position = 30
        # km/h
        self.speed = 1
        self.delta_x = 0

    def body(self):
        arcade.draw_circle_outline(self.x_position, self.y_position, 20, arcade.color.AIR_FORCE_BLUE, 1)

    def swim(self):
        """
        Algorithm: swim

        START
            IF player move to LEFT
                swim to left
            ELSE IF player move to RIGHT
                swim to right
            ELSE IF player move to up
                swim to up
            ELSE
                swim to down
        END
        """
        self.x_position += self.delta_x

    def on_draw(self):
        self.body()

    def update(self, delta_time: float):
        self.swim()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.delta_x = 10

        elif symbol == arcade.key.LEFT:
            self.delta_x = -10

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.delta_x = 0
