import os

# Unicode frame chars (defaults)
VERT_BORDER = "│"
HORIZ_BORDER = "─"
LU_CORNER = "┌"
LL_CORNER = "└"
RU_CORNER = "┐"
RL_CORNER = "┘"

# Types
Pos = tuple[int, int] | list[int, int]
Size = Pos

# Exceptions
class EngineError(Exception):
    pass

# Classes
# Graphics canvas
class Canvas:
    def __init__(self,
                size: Size,
                borders: dict = {
                        "vert": VERT_BORDER,
                        "horiz": HORIZ_BORDER,
                        "lu": LU_CORNER,
                        "ll": LL_CORNER,
                        "ru": RU_CORNER,
                        "rl": RL_CORNER
                     },
                 spacing: int = 0,
                 init_char: str = " "):
        assert size[0] > 0 and size[1] > 0, "Size should be 1 or bigger"

        self.size = size
        self.borders = borders
        self.spacing = spacing
        self.changes = dict()
        self.chars = [[init_char for _ in range(self.size[0])] for _ in range(self.size[1])]

        self.__init_draw()


    def __init_draw(self):
        # Draw the upper border
        print(self.borders["lu"] + \
            self.borders["horiz"] * (self.size[0] + self.spacing * 2) + \
            self.borders["ru"])

        # Draw the middle part(-s)
        for line in self.chars:
            print(self.borders["vert"] + \
                " " * self.spacing + \
                "".join(line) + \
                " " * self.spacing + \
                self.borders["vert"])

        # Draw the lower border
        print(self.borders["ll"] + \
            self.borders["horiz"] * (self.size[0] + self.spacing * 2) + \
            self.borders["rl"])


    # Draw the canvas on the screen (terminal)
    def draw(self):
        for pos, char in self.changes.items():
            self.chars[pos[1]][pos[0]] = char

            print(cursor_move(pos) + char, end="")

        # Clear the changes list (dict)
        self.changes = {}


    # Set a "pixel" to a specified value
    def set(self, pos: Pos, char: str):
        assert len(char) == 1, "Can only set single chars at a time"

        # self.chars[pos[1]][pos[0]] = char
        self.changes.update({(pos[0], pos[1]): char})


# Return an OS-specific escape sequence
def get_escape():
    if os.name == "posix":
        return "\033"
    else:
        raise EngineError("No support for Windows for now :(")

# Return a cursor moving escape sequence (to be printed)
def cursor_move(pos: Pos):
    escape = get_escape()

    line = pos[1] + 2  # Add 1 since 0th is border
    column = pos[0] + 2  # Also add 1

    return f"{escape}[{line};{column}H"
