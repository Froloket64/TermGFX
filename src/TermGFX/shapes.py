"""
Different shape implementations
to be used with the engine
"""

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

    @property
    def get_rect(self):
        return self.rect


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

        self.rect = tuple(tuple(self.char for _ in range(size[0])) for _ in range(size[1]))


# Class representing lines
class Line(BaseRect):
    def __init__(self, start: Pos, end: Pos, char: str, algorithm: str = "custom"):
        assert algorithm in ("custom", "dda"), "Unknown algorighm"

        self.char = char
        exec(f"self.rect = self._construct_{algorithm}(start, end, char)")


    # Draw a line using starting and ending positions [My custom algorihtm]
    @staticmethod
    def _construct_custom(start: Pos, end: Pos, char: str, rect: Rect | None = None) -> Rect:
        # Assertions
        assert start != end, "Must be not a dot"

        # Calculate travels
        dirs = "xy"

        distances_raw = tuple(map(lambda l: l[1] - l[0], zip(start, end)))

        distances = {
            distances_raw[0]: "x",
            distances_raw[1]: "y"
        }

        # Find the farthest one
        latest = tuple(distances.items())[0]
        for travel, dir in distances.items():
            if abs(travel) > abs(latest[0]):
                farthest = travel, dir
                shortest = latest
            else:
                farthest = latest
                shortest = travel, dir

            latest = travel, dir

        # Calculate the steps
        if farthest[0] > 0:
            step_farthest = 1
        elif farthest[0] < 0:
            step_farthest = 1
        else:
            step_farthest = 0

        if shortest[0] > 0:
            step_shortest = 1
        elif shortest[0] < 0:
            step_shortest = 1
        else:
            step_shortest = 0

        if shortest == farthest:
            shortest = farthest[0], dirs[dirs.index(farthest[1]) - 1]

        shortest_fraction = 1/farthest[0]  # FIXME: Division by zero
        move_at = 1/(abs(shortest[0]) + 1)

        # Actual line building
        if not rect:
            rect = [[" " for _ in range(abs(distances_raw[0]) + 1)] for _ in range(abs(distances_raw[1]) + 1)]

        pos = {
            "x": start[0],
            "y": start[1]
        }
        shortest_partial = 0

        while pos[farthest[1]] != end[dirs.index(farthest[1])]:
            rect[pos["y"]][pos["x"]] = char

            pos[farthest[1]] += step_farthest
            shortest_partial += shortest_fraction

            if shortest_partial >= move_at:
                shortest_partial = 0
                pos[shortest[1]] += step_shortest

        # Finish by drawing on `end` coordinate
        rect[end[1]][end[0]] = char


        return rect


    # Draw the line using DDA algorithm
    @staticmethod
    def _construct_dda(start: Pos, end: Pos, char: str, rect: Rect | None = None) -> Rect:
        '''
        # D = delta
        m = Dy / Dx

        steps = max(Dx, Dy)

        x_k+1, y_k+1 = {
            (
                x_k + 1,
                y_k + m
            ), m < 1
            (
                x_k + 1 / m,
                y_k + 1
            ), m > 1
            (
                x_k + 1,
                y_k + 1
            ), m = 1
        } (repeat `steps` times)
        '''

        distances = {
            "x": end[0] - start[0],
            "y": end[1] - start[1]
        }

        if not rect:
            # rect = [[" " for _ in range(abs(distances["x"]) + 1)] for _ in range(abs(distances["y"]) + 1)]
            rect = [[" " for _ in range(10)] for _ in range(10)]

        if not any([a == 0 for a in distances.values()]):
            # m = round(distances["y"] / distances["x"] + 0.01)
            m = distances["y"] / distances["x"]
            print(m)

            steps = max(distances.values())

            pos = {
                "x": start[0],
                "y": start[1]
            }

            old_pos = {
                "x": 0,
                "y": 0
            }

            # Actual line building
            for _ in range(steps):
                rect[pos["y"]][pos["x"]] = char

                print(pos)

                if abs(m) <= 1:
                    pos["x"] += 1
                    pos["y"] += round(m)
                else:
                    pos["x"] += round(1/m)
                    pos["y"] += 1


            rect[end[1]][end[0]] = char

        else:
            new_distances = {value: key for key, value in distances.items()}
            non_zero = list(filter(lambda x: x, distances.values()))
            non_zero.append(new_distances[non_zero[0]])

            for i in range(non_zero[0]):
                if non_zero[1] == "x":
                    rect[0][i] = char
                else:
                    rect[i][0] = char

        return rect


class Shape(Line):
    def __init__(self, *vertices: Pos, char: str, algorithm: str = "custom"):
        assert len(vertices) >= 3, "At least 3 vertices should be supplied"
        assert vertices[0] != vertices[-1], "Starting vertex shouldn't be repeated in the end"

        self.vertices = tuple(zip(vertices, vertices[1:] + vertices[:1]))
        self.char = char
        self.rect = None

        for start, end in self.vertices:
            exec(f"self.rect = self._construct_{algorithm}({start}, {end}, self.char, self.rect)")
