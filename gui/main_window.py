import tkinter as tk
from tkinter import ttk
from typing import List


class MainWindow:
    def __init__(self, title='') -> None:
        self.title = title

        self.root: tk.Tk = tk.Tk()
        self.tab_parent: ttk.Notebook = ttk.Notebook(
            self.root, style='lefttab.TNotebook'
        )
        self.tabs: List[tk.Frame] = []
        self.setup()

    def setup(self) -> None:
        style = ttk.Style(self.root)
        style.configure('lefttab.TNotebook', tabposition='nw')

        # default_font = tkinter.font.nametofont('TkDefaultFont')
        # default_font.config(size=10)

        self.tab_parent.pack(expand=1, fill='both')

    def add_frame(self, text: str) -> tk.Frame:
        frame = tk.Frame(self.tab_parent, bg='#fff')
        self.tab_parent.add(frame, text=text)
        self.tabs.append(frame)

        frame.configure(padx=10, pady=10, bg='#FFF')
        return frame

    def mainloop(self):
        # self.root.geometry('640x360')
        self.root.title(self.title)
        self.root.mainloop()
