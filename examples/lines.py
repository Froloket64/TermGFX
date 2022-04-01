from TermGFX.engine import Canvas
from TermGFX.shapes import Line


window_size = (20, 22)

canvas = Canvas(window_size)

line = Line((0, 0), (5, 8), "█", algorithm="dda")

line.draw(canvas)

canvas.draw(clear=False)
