from window import Window
from point import Point
from line import Line
from cell import Cell


if __name__ == "__main__":
    win = Window(800, 600)
    p1 = Point(50, 50)
    p2 = Point(250, 250)
    cell = Cell(50, 50, 250, 250)
    cell.set_window(win)
    cell.draw(fill="black", width=4)
    
    win.wait_for_close()
    