##  Some rects  ##

## Imports
from TermGFX.engine import Canvas
from TermGFX.shapes import BaseRect, FilledRect


# Defs
window_size = (25, 10)

rect1 = BaseRect((
    list("uwu"),
    list("kek")
))

rect2 = FilledRect((5, 4), "█")


# Main
canvas = Canvas(window_size)

canvas.draw()


rect1.draw(canvas, (5, 2))
rect2.draw(canvas, (14, 5))

canvas.draw()
