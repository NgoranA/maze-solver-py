from point import Line, Point
from window import Window


def main():
    win = Window(800, 600)
    p1 = Point(50, 50)
    p2 = Point(400, 400)
    line = Line(p2, p1)
    win.draw_line(line, "black")
    win.wait_for_close()


if __name__ == "__main__":
    main()
