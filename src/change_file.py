""" Module to create, delete, rename or change a file """

from os.path import abspath
from os import scandir

class HandleFiles:
    """ Handles files and workspace folder """
    def __init__(self):
        self.workspace_dir = abspath("../PTE/usercode")
        # REMIND: init required variables

    def return_latest_file(self) -> str:
        """ Return latest file """
        recent_file = self.find_latest_file()

        for line in open(recent_file, "rt", encoding="UTF-8"):
            print(line, end='')
        return recent_file

    def find_latest_file(self) -> str:
        """ Find latest file determined by date modified """
        recent_time = 0

        for entry in scandir(self.workspace_dir):
            if entry.is_file():
                date_modified = entry.stat().st_mtime_ns
                if  date_modified > recent_time:
                    recent_file = entry.name
                    recent_time = date_modified
        return abspath(self.workspace_dir + "/" + recent_file)
