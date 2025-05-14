import unittest
from maze import Maze
from window import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, Window(800, 600))
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def setUp(self):
        self.num_cols = 5
        self.num_rows = 4
        self.cell_size_x = 20
        self.cell_size_y = 20
        self.win = Window(400, 300)
        self.maze = Maze(0, 0, self.num_rows, self.num_cols, self.cell_size_x, self.cell_size_y, self.win)

    def test_maze_create_cells(self):
        self.assertEqual(len(self.maze._cells), self.num_cols)
        self.assertEqual(len(self.maze._cells[0]), self.num_rows)

    def test_maze_cell_coordinates(self):
        # Test the top-left cell's coordinates
        cell = self.maze._cells[0][0]
        self.assertEqual(cell._x1, 0)
        self.assertEqual(cell._y1, 0)
        self.assertEqual(cell._x2, self.cell_size_x)
        self.assertEqual(cell._y2, self.cell_size_y)

    def test_maze_cells_linked_to_window(self):
        for col in self.maze._cells:
            for cell in col:
                self.assertIsNotNone(cell._win)
                self.assertEqual(cell._win, self.win)

    def test_maze_draw_does_not_crash(self):
        # This simply checks that drawing all cells does not raise exceptions
        try:
            for i in range(self.num_cols):
                for j in range(self.num_rows):
                    self.maze._draw_cell(i, j)
        except Exception as e:
            self.fail(f"Drawing a cell raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()