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

    def test_break_entrance_and_exit(self):
        num_rows = 5
        num_cols = 5
        cell_size_x = 10
        cell_size_y = 10
        win = Window(200, 200)
        maze = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y, win)

        # Call the method under test
        maze._break_entrance_and_exit()

        entrance_cell = maze._cells[0][0]
        exit_cell = maze._cells[num_cols - 1][num_rows - 1]

        # Assert entrance top wall is removed
        self.assertFalse(entrance_cell.has_top_wall, "Entrance cell's top wall should be removed.")

        # Assert exit bottom wall is removed
        self.assertFalse(exit_cell.has_bottom_wall, "Exit cell's bottom wall should be removed.")

    def test_all_cells_visited_after_generation(self):
        """All cells should be marked visited after recursive wall breaking."""
        self.maze._break_walls_r(0, 0)
        for col in self.maze._cells:
            for cell in col:
                self.assertTrue(cell._visited, f"Unvisited cell found: {cell}")

    def test_wall_consistency_between_adjacent_cells(self):
        """Walls between adjacent cells should be consistent after maze generation."""
        self.maze._break_walls_r(0, 0)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                cell = self.maze._cells[i][j]
                # Check right neighbor
                if i < self.num_cols - 1:
                    right = self.maze._cells[i + 1][j]
                    self.assertEqual(cell.has_right_wall, right.has_left_wall,
                                     f"Inconsistent right/left wall at ({i}, {j})")
                # Check bottom neighbor
                if j < self.num_rows - 1:
                    below = self.maze._cells[i][j + 1]
                    self.assertEqual(cell.has_bottom_wall, below.has_top_wall,
                                     f"Inconsistent bottom/top wall at ({i}, {j})")

    def test_reset_cells_visited(self):
        self.maze._break_walls_r(0, 0)  # Visit all cells
        self.maze._reset_cells_visited()
        for col in self.maze._cells:
            for cell in col:
                self.assertFalse(cell._visited, f"Cell was not reset: {cell}")

    


if __name__ == "__main__":
    unittest.main()