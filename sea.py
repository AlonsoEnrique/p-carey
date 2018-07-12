from turtle import Turtle

import arcade


class Sea(arcade.Window):
    """ Sea

    turtle_population: POSITIVE INTEGER
    turtle: Turtle OBJECT
    divers: Diver OBJECT LIST
    is_enough_dives_hunting: BOOLEAN
    natural_sounds: STRING

    """
    def __init__(self):
        super(Sea, self).__init__(title="Turtle carey, the game")
        self.turtle_population = None
        self.turtle = None
        self.dives = None
        self.is_enough_dives_hunting = None
        self.natural_sounds = None

    def setup(self):
        self.natural_sounds = arcade.load_sound('sounds/mainmenu.mp3')
        arcade.play_sound(self.natural_sounds)

        # GET this value from API in the cloud
        self.turtle_population = 10

        self.turtle = Turtle()
        # TODO: Generate initial dives

    def on_draw(self):
        arcade.start_render()
        self.turtle.on_draw()

    def update(self, delta_time: float):
        """
        Algorithm: update
        Description: This algorithm is a loop when the main actions happen

        START
            game_over()
            won()

            enough_hunting_dives()

            turtle.movement()
        END
        """
        self.game_over()
        self.won()

        self.enough_hunting_dives()

        self.turtle.update(delta_time)

    def on_key_press(self, symbol: int, modifiers: int):
        self.turtle.on_key_press(symbol=symbol, modifiers=modifiers)

    def on_key_release(self, key: int, modifiers: int):
        self.turtle.on_key_release(key=key, modifiers=modifiers)

    def game_over(self):
        """
        Algorithm: game_over

        START
            IF turtle is touch for divers
                RETURN True
            ELSE
                RETURN False
        END
        """
        return False

    def won(self):
        """
        Algorithm: won

        START
            IF turtle reach final
                RETURN True
            ELSE
                RETURN False
        END
        """
        pass

    def enough_hunting_dives(self):
        """
        Algorithm: enough_dives_hunting

        START
            IF exists enough dives hunting (enough_dives_hunting) the turtle
                GENERATE dives

        END
        """
        pass
