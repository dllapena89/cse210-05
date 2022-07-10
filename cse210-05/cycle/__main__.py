import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Cycle"
BLACK = Color(0, 0, 0)
LIME = Color(0, 255, 0)
RED = Color(255, 0, 0)

# Main

def main():
    
    cast = Cast()

    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(BLACK)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
# create player 1
    x = int(MAX_X * 0.25)
    y = int(MAX_Y / 2)
    position1 = Point(x, y)

    player1 = Actor()
    player1.set_text("#")
    player1.set_font_size(FONT_SIZE)
    player1.set_color(RED)
    player1.set_position(position1)
    cast.add_actor("player1", player1)

# create player 2
    x = int(MAX_X * 0.75)
    y = int(MAX_Y / 2)
    position2 = Point(x, y)

    player2 = Actor()
    player2.set_text("#")
    player2.set_font_size(FONT_SIZE)
    player2.set_color(LIME)
    player2.set_position(position2)
    cast.add_actor("player2", player2)

# start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()