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

    def set_window(self, window):
        self._win = window

    def draw(self, **style_kwargs):
        if self._win is None:
            raise ValueError("Window not set. Use set_window() to set the window before drawing.")
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), **style_kwargs)
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), **style_kwargs)
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), **style_kwargs)
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), **style_kwargs)

    def __repr__(self):
        return f"Cell({self._x1}, {self._y1}, {self._x2}, {self._y2})"