"""
Different shape implementations
to be used with the engine
"""

import math

## Types
Size = tuple[int, int]
Pos = tuple[int, int]
Rect = tuple[tuple[str]] | list[list[str]]


## Classes
# A base class for all other shapes
class BaseRect:
    def __init__(self, chars: tuple[tuple[str]]):
        assert max(map(len, chars)) == min(map(len, chars)), "All columns should be the same size"

        self.rect = chars


    def __str__(self):
        sep = "\n  "  # As for Python 3.10, \'es are not supported in f-strings

        return f"""{type(self).__name__}(
  {sep.join(["".join(line) for line in self.rect])}
)"""


    @property
    def size(self):
        return (
            len(self.rect[0]),
            len(self.rect)
        )

    def get_rect(self):
        return self.rect

    def set_pixel(self, pos: Pos, char: str):
        self.rect[pos[1]][pos[0]] = char

    def draw(self, surface, pos: Pos = (0, 0)):
        assert not any(
                map(
                    lambda l: l[0] > l[1],
                    zip(self.size, surface.size)
                )
            ), "Rect size bigger than canvas"

        for y, line in enumerate(self.rect):
            for x, char in enumerate(line):
                if char != " ":
                    surface.set((x + pos[0], y + pos[1]), char)


# A rectangular area filled with a single char
class FilledRect(BaseRect):
    def __init__(self, size: Size, char: str):
        assert len(char) == 1, "You can pass only a single char"

        self.char = char

        self.rect = list(list(self.char for _ in range(size[0])) for _ in range(size[1]))


# Class representing lines
class Line(BaseRect):
    def __init__(self, start: Pos, end: Pos, char: str, algorithm: str = "custom"):
        assert algorithm in ("custom", "bresenham"), "Unknown algorighm"

        self.char = char
        self.rect_size = tuple(map(max, ((start[0], end[0]), (start[1], end[1]))))

        exec(f"self.rect = self._construct_{algorithm}(start, end, char)")

    # A yet another implementation...
    def _construct_custom(self, start: Pos, end: Pos, char: str):
        """
        y = mx + b
        """

        # Prepare a rect to draw on and return later
        # rect = FilledRect(self.rect_size, " ")
        rect = FilledRect(list(map(lambda x: x + 10, self.rect_size)), " ")

        # Calculate `m` (slope) using `b` equality
        """ Reference:
        { y1 = x1m + b
        { y2 = x2m + b

        { b = y1 - x1m
        { b = y2 - x2m

        y1 - x1m = y2 - x2m

        y1 - y2 = x1m - x2m = m(x1 - x2)

        m = (y1 - y2) / (x1 - x2) (= (y2 - y1) / (x2 - x1), since the signs are mirrored)
        """

        m = (end[1] - start[1]) // (end[0] - start[0])

        # Draw the initial point (`start`)
        rect.rect[start[1]][start[0]] = char

        # FIXME
        x, y = start
        if abs(m) < 1:
            while (x, y) != end:
                x += int(math.copysign(1, m))
                y = x//abs(m)

                rect.rect[y][x] = char
        else:
            while (x, y) != end:
                x = y//abs(m)
                y += int(math.copysign(1, m))

                rect.rect[y][x] = char

        return rect.rect


    def _construct_bresenham(self, start: Pos, end: Pos, char: str):
        # Reference: https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm

        # Calculate the deltas for each coordinate
        delta = {
            "x": end[0] - start[0],
            "y": end[1] - start[1]
        }

        # Prepare a Rect to be filled
        rect = FilledRect(list(map(lambda x: x + 10, self.rect_size)), " ")

        if delta["x"] > delta["y"]:
            # Calculate the error (doubled, for int arithmetic)
            error = 2 * delta["y"] - delta["x"]

            y = start[1]

            for x in range(start[0], end[0]+1):
                # Plot the resulting pixel
                rect.set_pixel((x, y), char)

                # If the error is positive
                if error > 0:
                    # Increment `y`
                    y += 1

                    # And subtract 2dx from the error
                    error -= 2 * delta["x"]

                # Increase error by 2dy
                error += 2 * delta["y"]
        else:  # Swap the coordinates
            # Calculate the error (doubled, for int arithmetic)
            error = 2 * delta["x"] - delta["y"]

            x = start[0]

            for y in range(start[1], end[1]+1):
                # Plot the resulting pixel
                rect.set_pixel((x, y), char)

                # If the error is positive
                if error > 0:
                    # Increment `x`
                    x += 1

                    # And subtract 2dx from the error
                    error -= 2 * delta["y"]

                # Increase error by 2dy
                error += 2 * delta["x"]

        return rect.get_rect()


class Shape(Line):  # FIXME
    def __init__(self, *vertices: Pos, char: str, algorithm: str = "custom"):
        assert len(vertices) >= 3, "At least 3 vertices should be supplied"
        assert vertices[0] != vertices[-1], "Starting vertex shouldn't be repeated in the end"

        self.vertices = tuple(zip(vertices, vertices[1:] + vertices[:1]))
        self.char = char
        self.rect = None

        for start, end in self.vertices:
            exec(f"self.rect = self._construct_{algorithm}({start}, {end}, self.char, self.rect)")
