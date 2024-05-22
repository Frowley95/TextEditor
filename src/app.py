"""Module for quick-edit app"""

import os
import tkinter
from os import scandir
from os.path import abspath
from tkinter import Menu, filedialog, END, Text, ttk
from tkinter.messagebox import showinfo

current_file = ""


def open_file(file) -> None:
    """Open a file"""

    global current_file
    current_file = file

    with open(current_file, 'r', encoding="UTF-8") as file:
        file = file.read()

    Textbox.textbox.delete("1.0", END)
    Textbox.textbox.insert(END, file)


class App(tkinter.Tk):
    """App initialisation"""

    def __init__(self):
        super().__init__()

        self.workspace_dir = abspath("../workspace/")

        app_width, app_height = self.winfo_screenwidth() // 2, self.winfo_screenheight() // 2
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()

        mid_x = (screen_width - app_width) // 2
        mid_y = (screen_height - app_height) // 2

        self.title("Text Editor")
        self.iconbitmap(abspath('../data/favicon.ico'))
        self.geometry(f'{app_width}x{app_height}+{mid_x}+{mid_y}')

        FileTree(self)
        Textbox(self)
        Navbar(self)
        Startup(self, self.workspace_dir)

        self.mainloop()


class FileTree(ttk.Frame):
    """File tree display"""

    def __init__(self, parent):
        super().__init__(parent)

        ttk.Label(self, background='white', foreground='black').pack(expand=True, fill='both')
        self.place(x=0, y=0, relwidth=0.3, relheight=1)


class Navbar(ttk.Frame):
    """Navigation bar display"""

    def __init__(self, parent):
        super().__init__(parent)

        menu_bar = Menu(self)
        parent.config(menu=menu_bar)

        self.create_navbar(menu_bar)

    def create_navbar(self, menu_bar):
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open (Ctrl+O)", command=self.menu_open_file)
        file_menu.add_command(label="Open Folder", command=self.menu_open_folder)
        file_menu.add_command(label="Save (Ctrl+S)", command=self.menu_save_file)
        file_menu.add_command(label="Save As", command=self.menu_save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=quit)

        edit_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo (Ctrl+Z)", command=self.menu_undo_edit)
        edit_menu.add_command(label="Redo (Ctrl+Y)", command=self.menu_redo_edit)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut (Ctrl+X)", command=self.menu_cut_edit)
        edit_menu.add_command(label="Copy (Ctrl+C)", command=self.menu_copy_edit)
        edit_menu.add_command(label="Paste (Ctrl+V)", command=self.menu_paste_edit)

    @staticmethod
    def menu_open_file():
        """Opens file and returns it's content"""

        file = filedialog.askopenfilename(filetypes=[("all files", "*.*")],
                                          initialdir="../workspace/",
                                          title="Open file")
        if file:
            open_file(file)

    def menu_open_folder(self):
        pass

    @staticmethod
    def menu_save_file():
        """Saves file"""

        global current_file

        file = open(current_file, 'w')
        file.write(Textbox.textbox.get(1.0, END))

        file.close()

    @staticmethod
    def menu_save_as_file():
        """Saves file as"""

        file = filedialog.asksaveasfilename(filetypes=[("all files", "*.*")],
                                            initialdir="../workspace/",
                                            title="Save file")
        if file:
            filename = file
            filename = filename.replace("../workspace/", "")

            file = open(filename, 'w')
            file.write(Textbox.textbox.get(1.0, END))

            file.close()

    def menu_undo_edit(self):
        pass

    def menu_redo_edit(self):
        pass

    def menu_cut_edit(self):
        pass

    def menu_copy_edit(self):
        pass

    def menu_paste_edit(self):
        pass


class Textbox(ttk.Frame):
    """Text box display"""

    textbox = None

    def __init__(self, parent):
        super().__init__(parent)

        Textbox.textbox = Text(parent)
        Textbox.textbox.pack(expand=True, fill='both')
        Textbox.textbox.place(relx=0.3, y=0, relwidth=0.7, relheight=1)


class Startup(ttk.Frame):
    """Initialize the app"""

    def __init__(self, parent, workspace_dir):
        super().__init__(parent)

        self.workspace_dir = workspace_dir

        self.return_latest_file()

    def find_latest_file(self):
        """Find latest file determined by date modified"""

        recent_time = 0
        recent_file = ""

        if not os.path.exists(self.workspace_dir):  # If no workspace dir exists, make one and return
            os.mkdir(self.workspace_dir)
            return

        if not os.listdir(self.workspace_dir):  # If no entry exists, return
            return

        for entry in scandir(self.workspace_dir):
            if entry.is_file():
                date_modified = entry.stat().st_mtime_ns

                if date_modified > recent_time:
                    recent_file = entry.name
                    recent_time = date_modified

        return abspath(self.workspace_dir + "/" + recent_file)

    def return_latest_file(self):
        """Return latest file"""

        recent_file_abspath = self.find_latest_file()

        if recent_file_abspath is None:
            showinfo("File not found", "Please select a file to use!")
            requested_file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py"),
                                                                   ("All Files", "*.*")],
                                                        initialdir=self.workspace_dir,
                                                        title="Select a text file")

            if requested_file == "":  # If no file is selected, don't display any file
                return
            else:
                recent_file_abspath = abspath(requested_file)

        global current_file
        current_file = recent_file_abspath

        with open(current_file, 'rt', encoding="UTF-8") as file:
            file = file.read()

        Textbox.textbox.insert(END, file)
