""" Module providing the user window display. """

import tkinter as ttk

# REMIND: Import only required methods once known
from change_file import HandleFiles

# REMIND: CREATE INTERFACES FOR COMMUNICATION.

class UserWindow:
    """ Initializes root window """
    def __init__(self):
        root = ttk.Tk()
        root.title("Text Editor")
        self.create_nav_bar()
        self.file_into_textbox()

        # Start the event loop.
        root.mainloop()

    def create_nav_bar(self):
        """ Initializes navigation bar """
        print("Test: End of create_nav_bar")
    def file_into_textbox(self):
        """ Opens latest file if it exists. Else, create new file menu. """
        file_handle = HandleFiles()
        latest_file = file_handle.return_latest_file()
        print(latest_file)
        if latest_file == "" or latest_file is None:
            pass # No old file found. REMIND: Display menu to create a new one.
        print("Test: End of open_file")
