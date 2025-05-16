from cell import Cell
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        seed=None,
        ):

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

        if seed is not None:
            random.seed(seed)

    def _create_cells(self):
        for i in range(self._num_cols):
            cols = []
            for j in range(self._num_rows):
                x1 = self._x1 + i * self._cell_size_x
                y1 = self._y1 + j * self._cell_size_y
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                cell = Cell(x1, y1, x2, y2)
                cell.set_window(self._win)
                cols.append(cell)
            self._cells.append(cols)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
            

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell.draw(fill="black", width=4)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)
        
        exit_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        exit_cell.has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current._visited = True
        while True:
            visit_index = []
            up = self._cells[i][j - 1] if j > 0 else None
            down = self._cells[i][j + 1] if j < self._num_rows - 1 else None
            left = self._cells[i - 1][j] if i > 0 else None
            right = self._cells[i + 1][j] if i < self._num_cols - 1 else None
            if up and not up._visited:
                visit_index.append(((i, j - 1), "up"))
            if down and not down._visited:
                visit_index.append(((i, j + 1), "down"))
            if left and not left._visited:
                visit_index.append(((i - 1, j), "left"))
            if right and not right._visited:
                visit_index.append(((i + 1, j), "right"))
            if not visit_index:
                current.draw()
                return
            next_direction = random.choice(visit_index)
            next_cell_i, next_cell_j = next_direction[0]
            next_cell = self._cells[next_cell_i][next_cell_j]
            direction = next_direction[1]
            if direction == "up":
                current.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif direction == "down":
                current.has_bottom_wall = False
                next_cell.has_top_wall = False
            elif direction == "left":
                current.has_left_wall = False
                next_cell.has_right_wall = False
            elif direction == "right":
                current.has_right_wall = False
                next_cell.has_left_wall = False
            self._break_walls_r(next_cell_i, next_cell_j)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j]._visited = False
