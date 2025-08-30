import tkinter as tk
from tkinter import ANCHOR, ttk

class viewer(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        window_width = 300
        window_height = 0

        # get the screen dimension
        screen_width = self.winfo_screenwidth()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = 0

        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')        
        

        self.title("         JARVIS")
        self.iconbitmap('G:\PYTHON\Python Programs\JARVIS\jarvis_icon.ico')
        self.resizable(0, 0)
        self.attributes('-topmost', 1)




if __name__ == "__main__":
    view = viewer()
    view.mainloop()        