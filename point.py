class Point:
    def __init__(self, x, y):
        self.x = x  # left of the screen
        self.y = y  # top of the screen


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1  # left of the screen
        self.p2 = p2  # top of the screen

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
