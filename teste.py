from tkinter import *
from tkinter import ttk


class window_1():
    def __init__(self):
        self.root = Tk()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = 400
        window_height = 200

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f'{window_width}x{window_height}+{x}+{y}')
        self.root.resizable(False, False)

        self.window = ttk.Frame(self.root, padding=10)
        self.window.grid()

        ttk.Label(self.window, text='Olá', font='_ 15').grid(column=0, row=0)
        ttk.Button(self.window).grid(column=0, row=1)

        self.root.mainloop()

window_1()