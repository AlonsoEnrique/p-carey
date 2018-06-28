import arcade

from diver import Diver
from turtle import Turtle

""" Sea

turtle_population: POSITIVE INTEGER
turtle: Turtle OBJECT
divers: Diver OBJECT LIST
is_enough_dives_hunting: BOOLEAN
natural_sounds: STRING

Algorithm: update
Description:
This algorithm is a loop when the main actions happen

START    
    game_over()
    won()

    enough_hunting_dives()    

    turtle.movement()    
END


Algorithm: game_over

START
    IF turtle is touch for divers
        RETURN True
    ELSE
        RETURN False
END

Algorithm: won

START
    IF turtle reach final
        RETURN True
    ELSE
        RETURN False
END

Algorithm: enough_dives_hunting

START
    IF exists enough dives hunting (enough_dives_hunting) the turtle
        GENERATE dives

END

"""


class Sea(arcade.Window):
    pass
