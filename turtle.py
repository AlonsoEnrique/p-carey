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
        # km/h
        self.speed = 1

    def body(self):
        arcade.draw_circle_outline(100, 200, 16, arcade.color.AIR_FORCE_BLUE, 1)

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
        raise NotImplementedError

    def on_draw(self):
        self.body()
