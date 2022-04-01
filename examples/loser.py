## DISCL.: It's just a dumb joke, it's not supposed to mean anything ##

from TermGFX.engine import Canvas
from time import sleep


window_size = (20, 5)

canvas = Canvas(window_size, init_char="_")

lines = (
    (
        ((1, 1), "U"),
    ),
    (
        ((1, 2), "a"),
        ((2, 2), "r"),
        ((3, 2), "e"),
    ),
    (
        ((5, 2), "a"),
    ),
    (
        ((1, 3), "l"),
        ((2, 3), "o"),
        ((3, 3), "s"),
        ((4, 3), "e"),
        ((5, 3), "r"),
    ),
    (
        ((1, 4), ":"),
        ((2, 4), ")"),
    )
)

canvas.draw()

for line in lines:
    for char in line:
        canvas.set(*char)

    canvas.draw()

    sleep(0.5)
