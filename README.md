TermGFX
-------

A yet another terminal graphics library written in Python.

# Why tho?
The idea behind this project is to allow simple yet extensible graphics processing in the terminal. I'm a videogames enjoyer and I have used libraries such as PyGame, so it was an inspiration for me to write my own graphics lib. I decided using a terminal/TTY as canvas, because I spend a lot of time sitting at it as a Linux user. Moreover, it felt like something a bit more unique ~~(even though there were a bunch of such project already, shh)~~

# What it can
Draw
+ **Dots** 
+ **Lines**

# What's planned
+ **Cirle** shapes
+ **Arbitrary** shapes (with straight sides)

# Installation
## Prerequisites
In order to use the package, you need **Python 3**
+ Python (3.6+)* (Some examples use 3.10, though)

\* If incorrect, please report _(too lazy to figure out actual range of versions needed)_

## pip
You can use `pip` or `pip3` to install **TermGFX** by executing
``` sh
pip --user install termgfx
```
**Note:** you can omit `--user`, but it's not recommended (see [why][https://stackoverflow.com/questions/42988977/what-is-the-purpose-of-pip-install-user])

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
