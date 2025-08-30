


import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x110')
        self.resizable(0, 0)
        self.title('Login')

        # UI options
        paddings = {'padx': 5, 'pady': 5}
        entry_font = {'font': ('Helvetica', 11)}

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        username = tk.StringVar()
        password = tk.StringVar()

        # username
        username_label = ttk.Label(self, text="Username:")
        username_label.grid(column=0, row=0, sticky=tk.W, **paddings)

        username_entry = ttk.Entry(self, textvariable=username, **entry_font)
        username_entry.grid(column=1, row=0, sticky=tk.E, **paddings)

        # password
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(column=0, row=1, sticky=tk.W, **paddings)

        password_entry = ttk.Entry(
            self, textvariable=password, show="*", **entry_font)
        password_entry.grid(column=1, row=1, sticky=tk.E, **paddings)

        # login button
        login_button = ttk.Button(self, text="Login")
        login_button.grid(column=1, row=2, sticky=tk.E, **paddings)

        # configure style
        self.style = ttk.Style(self)
        self.style.configure('TLabel', font=('Helvetica', 11))
        self.style.configure('TButton', font=('Helvetica', 11))


if __name__ == "__main__":
    app = App()
    app.mainloop()


# import tkinter as tk

# root = tk.Tk()
# root.title('Tkinter Window Demo')
# root.geometry('600x400+50+50')
# # root.resizable(False, False)
# root.attributes('-alpha',0.1)

# root.title('Tkinter Window Demo')
# root.resizable(0, 0)
# root.attributes('-topmost', 1)

# root.mainloop()


'''
import tkinter as tk


root = tk.Tk()
root.title('Tkinter Window - Center')

window_width = 300
window_height = 200

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print (screen_height," ",screen_width)
# find the center point
center_x = int(screen_width/2 - window_width / 2)
# center_y = int(screen_height/2 - window_height / 2)
center_y = 0

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
# root.geometry()


root.mainloop()
'''