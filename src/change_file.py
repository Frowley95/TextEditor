""" Module to create, delete, rename or change a file """

from os.path import abspath
from os import scandir

class HandleFiles:
    """ Handles files and workspace folder """
    def __init__(self):
        self.workspace_dir = abspath("../PTE/usercode")

    def return_latest_file(self) -> str:
        """ Return latest file """
        recent_file = self.find_latest_file()
        content_file = self.open_file(recent_file)
        return content_file

# Remind: Implement keyboard shortcuts (Observer/listener)

    def open_file(self, file) -> str:
        """ Opens file and returns it's content. """
        with open(file, "rt", encoding="UTF-8") as read_file:
            return read_file.read()

    def save_file(self):
        """ Save user defined file """
        print("File has been saved!")

    def undo_edit(self):
        """ Undo in user active file """
        print("Edit has been undone!")

    def redo_edit(self):
        """ Redo in user active file """
        print("Redo has been done!")

    def cut_edit(self):
        """ Cut user active select """
        print("Cut has been done!")

    def copy_edit(self):
        """ Copy user active select """
        print("Copy has been done!")

    def paste_edit(self):
        """ Paste user active select """
        print("Paste has been done!")

    def find_latest_file(self) -> str:
        # REMIND: Remake to save current file/workspace on quit instead of iteration
        """ Find latest file determined by date modified """
        recent_time = 0
        for entry in scandir(self.workspace_dir):
            if entry.is_file():
                date_modified = entry.stat().st_mtime_ns
                if  date_modified > recent_time:
                    recent_file = entry.name
                    recent_time = date_modified
        return abspath(self.workspace_dir + "/" + recent_file)
