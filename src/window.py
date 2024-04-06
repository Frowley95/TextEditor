""" Module providing the user window display. """

from tkinter import Tk, Menu, filedialog, Text, END
from tkinter.messagebox import showinfo
from os.path import abspath

from change_file import HandleFiles

class UserWindow:
    """ Initializes root window """
    def __init__(self):
        super().__init__()
        root = Tk()
        root.title("Text Editor")
        root.iconbitmap(abspath("../PTE/.data/favicon.ico"))

        self.nav_bar(root)
        self.init_textbox(root)

        # Start the event loop.
        root.mainloop()

    def nav_bar(self, root):
        """ Initializes navigation bar """
        menu_bar = Menu(root)
        root.config(menu = menu_bar)

        file_menu = Menu(menu_bar, tearoff = 0)
        menu_bar.add_cascade(label = "File", menu = file_menu)
        file_menu.add_command(label = "Open (Ctrl+O)", command = HandleFiles.open_file)
        file_menu.add_command(label = "Save (Ctrl+S)", command = HandleFiles.save_file)
        file_menu.add_separator()
        file_menu.add_command(label = "Exit", command = quit)

        edit_menu = Menu(menu_bar, tearoff = 0)
        menu_bar.add_cascade(label = "Edit", menu = edit_menu)
        edit_menu.add_command(label = "Undo (Ctrl+Z)", command = HandleFiles.undo_edit)
        edit_menu.add_command(label = "Redo (Ctrl+Y)", command = HandleFiles.redo_edit)
        edit_menu.add_separator()
        edit_menu.add_command(label = "Cut (Ctrl+X)", command = HandleFiles.cut_edit)
        edit_menu.add_command(label = "Copy (Ctrl+C)", command = HandleFiles.copy_edit)
        edit_menu.add_command(label = "Paste (Ctrl+V)", command = HandleFiles.paste_edit)

    def init_textbox(self, root):
        """ Initialize textbox and display file. """
        textbox = Text(root, width=60, height=20)
        textbox.pack(pady=5)
        self.file_into_textbox(root, textbox)

    def file_into_textbox(self, root, textbox):
        """ Opens latest file if it exists. Else, create new file menu. """
        file_handle = HandleFiles()
        latest_file = file_handle.return_latest_file()
        if latest_file == "" or latest_file is None: # REMIND: Edit to create file instead of find.
            showinfo("File not found", "Please select a file to use!")
            root.filename = filedialog.askopenfile(filetypes=[("all files", "*.*")],
                                                    initialdir="../PTE/usercode/",
                                                    title="Select a text file")
            # REMIND: Open the selected file in textbox
        textbox.insert(END, latest_file)
        print("Test: End of open_file")
