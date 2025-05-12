from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Tkinter Window")

        self.__canvas = Canvas(self.__root, width=width, height=height, bg="white")
        self.__canvas.pack(pady=20, fill=BOTH, expand=True)

        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, **style_kwargs):
        line.draw(self.__canvas, **style_kwargs)
        self.redraw()
    