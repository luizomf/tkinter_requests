# import os
import tkinter as tk
from tkinter import filedialog
from gui.main_window import MainWindow
from typing import Iterable, Tuple


class TkFrame:
    def __init__(self, parent: MainWindow, frame_name: str) -> None:
        self.parent = parent
        self.frame: tk.Frame = self.parent.add_frame(frame_name)

    def add_label(self, text: str, parent=None) -> tk.Label:
        """Add tk.Label"""
        parent = parent or self.frame
        label = tk.Label(
            parent, text=text, relief='flat', bg='#FFF', bd=0,
            fg='#282a36', width=15, padx=5, pady=5, anchor='w',
            font=('Helvetica', 12, 'bold'),
        )
        return label

    def add_entry(self, parent=None) -> Tuple[tk.Entry, tk.StringVar]:
        """Add tk.Entry"""
        string_var = tk.StringVar('')
        parent = parent or self.frame

        entry = tk.Entry(
            parent, highlightthickness=1, highlightcolor='#282a36',
            highlightbackground='#ccc', fg='#282a36', relief='flat',
            font=('Helvetica', 12, 'normal'), textvariable=string_var,
            borderwidth=10
        )

        return entry, string_var

    def add_button(self, text: str, command=None, parent=None) -> tk.Button:
        """Add tk.Button"""
        parent = parent or self.frame
        button = tk.Button(
            parent, text=text.upper(), command=command, pady=5, padx=50,
            bg='#282a36', fg='#8be9fd', activebackground='#282a36',
            activeforeground='#8be9fd', font=('Helvetica', 10, 'bold'),
            borderwidth=0, cursor='hand2'
        )
        return button

    def add_text(self, parent=None) -> tk.Text:
        """Add tk.Entry

        To insert text = text.insert('insert', 'texto')
        To get text = text.get('1.0', 'end')
        """
        parent = parent or self.frame
        text = tk.Text(
            parent, height=5, highlightthickness=1,
            highlightcolor='#8be9fd', highlightbackground='#282a36',
            insertbackground='#8be9fd', selectbackground='#8be9fd',
            inactiveselectbackground='#8be9fd', selectforeground='#282a36',
            bg='#282a36', fg='#8be9fd', relief='flat',
            font=('Courier', 12, 'normal'), borderwidth=10
        )

        text.bind('<Tab>', lambda arg: self._fix_text_tab(text))
        return text

    def _fix_text_tab(self, text: tk.Text):
        """Change tabsize to spaces"""
        text.insert('insert', ' ' * 2)
        return 'break'

    def add_file_dialog(
        self, text: str, parent=None
    ) -> Tuple[tk.Button, tk.StringVar]:
        """Add file dialog"""
        parent = parent or self.frame
        path = tk.StringVar()
        btn = self.add_button(text, parent=parent)
        btn.configure(command=lambda: self._open_file(path, btn))
        return btn, path

    def _open_file(self, path, button):
        """Internal function to file dialog"""
        file_paths = filedialog.askopenfilename(
            initialdir='./', title="Selecione o arquivo",
            filetypes=(
                ("Qualquer arquivo", "*.*"), ("JPG", "*.jpg"),
                ("PNG", "*.png"),
            )
        )

        if not file_paths:
            return

        # file_names = ',\n'.join([os.path.basename(p) for p in file_paths])
        path.set(file_paths)
        # button.configure(text=file_names)

    def add_dropdown(
        self, options: Iterable = [], parent=None
    ) -> Tuple[tk.OptionMenu, tk.StringVar]:
        """Add dropdown"""
        parent = parent or self.frame
        string_var = tk.StringVar('')

        option_menu = tk.OptionMenu(
            parent,
            string_var,
            *options
        )

        option_menu.configure(
            highlightthickness=0, borderwidth=0, highlightcolor='#282a36',
            highlightbackground='#ccc', fg='#282a36', relief='flat',
            font=('Courier', 12, 'normal'), anchor='w'
        )

        menu = option_menu.nametowidget(option_menu.menuname)
        menu.configure(
            fg='#282a36', relief='flat', font=('Courier', 12, 'normal'),
        )

        return option_menu, string_var

    def add_frame(self, parent=None) -> tk.Frame:
        parent = parent or self.frame
        frame = tk.Frame(parent)
        return frame
