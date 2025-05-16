from window import Window
from maze import Maze


if __name__ == "__main__":
    win = Window(800, 600)
    maze = Maze(20, 20, 14, 19, 40, 40, win)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cells_visited()
    maze.solve()

    
    win.wait_for_close()
    