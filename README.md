TermGFX
-------

A yet another terminal graphics written in Python.

# What it can
Draw
+ **Dots** 
+ **Lines** (poorly, for now) 

# What's planned
+ Adequate **Line** drawing
+ **Cirle** shapes
+ **Arbitrary** shapes (with straight sides)

# Installation
## Prerequisites
In order to use the package, you need **Python 3**
+ Python (3.6+)*

\* If incorrect, please report _(too lazy to figure out actual range of versions needed)_

## pip
You can use `pip` or `pip3` to install **TermGFX** by executing
``` sh
pip --user install termgfx
```

## From source
The source code is located in `<project root>/src/TermGFX/`, so, in order to use it, you might just copy the file onto yout project directory, though it's not recommended (`pip` is a better option)

# Usage
To get more information on project usage, you can view examples located in `<project root>/examples/`

Here's an overview:
First, import the `Canvas`
``` python
from TermGFX.engine import Canvas
```
Then, create a `Canvas` instance
``` python
window_size = (20, 10)  # Size of the canvas

canvas = Canvas(window_size)  # Instantiate a canvas with the size of (20, 10)
```

## Pixels
Now you can set "pixels" on the canvas
``` python
char = "O"  # A character to be displayed

canvas.set((0, 0), char)  # Set (0, 0) pixel to "O" 
```
And draw the canvas on the "screen"
``` python
canvas.draw()
```

## Shapes
For all shapes, see `shapes.py`
Example: Drawing a rectangle filled with "$" chars:
``` python
from TermGFX.engine import Canvas
from TermGFX.shapes import FilledRect

canvas = Canvas((20, 10))
rect = FilledRect((5, 2), "$")

rect.draw(canvas)
canvas.draw()
```

_**Tip:** shapes usually have a `draw` method that allows for easy drawing on a surface_