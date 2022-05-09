from TermGFX.engine import Canvas
from TermGFX.shapes import Shape


window_size = (50, 50)

canvas = Canvas(window_size)

tri = Shape(
    (20, 0),
    (18, 2),
    (22, 2)
)

tri.draw(canvas)

canvas.draw()
