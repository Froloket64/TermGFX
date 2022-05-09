from TermGFX.engine import Canvas
from TermGFX.shapes import Line

window_size = (20, 22)

canvas = Canvas(window_size)

lines = []

lines.append(Line((0, 0), (5, 8)))
lines.append(Line((0, 0), (0, 8)))
lines.append(Line((0, 8), (5, 8)))
lines.append(Line((10, 10), (1, 12)))

for line in lines:
    line.draw(canvas)

canvas.draw()
