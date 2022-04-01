import os

# Unicode frame chars (defaults)
VERT_BORDER = "│"
HORIZ_BORDER = "─"
LU_CORNER = "┌"
LL_CORNER = "└"
RU_CORNER = "┐"
RL_CORNER = "┘"


class Canvas:
    def __init__(self,
                size: tuple[int, int],
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
        self.chars = [[init_char for _ in range(self.size[0])] for _ in range(self.size[1])]


    # Draw the canvas on the screen (terminal)
    def draw(self, *, clear: bool = True):
        # Clear the screen
        if clear:
            os.system("clear")

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


    # Set a "pixel" to a specified value
    def set(self, pos: tuple[int, int], char: str):
        assert len(char) == 1, "Can only set single chars at a time"

        self.chars[pos[1]][pos[0]] = char
