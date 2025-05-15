from point import Point
from line import Line


class Cell:
    def __init__(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = None
        self._visited = False

    def set_window(self, window):
        self._win = window

    def draw(self, **style_kwargs):
        if self._win is None:
            raise ValueError("Window not set. Use set_window() to set the window before drawing.")
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), **style_kwargs)
        else:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), fill="#d9d9d9", width=0)
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), **style_kwargs)
        else:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), fill="#d9d9d9", width=0)
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), **style_kwargs)
        else:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), fill="#d9d9d9", width=0)
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), **style_kwargs)
        else:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), fill="#d9d9d9", width=0)

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            raise ValueError("Window not set. Use set_window() to set the window before drawing.")
        color = "gray" if undo else "red"
        self._win.draw_line(Line(Point((self._x1 + self._x2)/2, (self._y1 + self._y2)/2), Point((to_cell._x1 + to_cell._x2)/2, (to_cell._y1 + to_cell._y2)/2)), fill=color, width=4)

    def __repr__(self):
        return f"Cell({self._x1}, {self._y1}, {self._x2}, {self._y2})"