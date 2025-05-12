class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, **style_kwargs):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, **style_kwargs)

    def __repr__(self):
        return f"Line({self.point1}, {self.point2})"

    def __eq__(self, other):
        return (self.point1 == other.point1 and self.point2 == other.point2) or (self.point1 == other.point2 and self.point2 == other.point1)