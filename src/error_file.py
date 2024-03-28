""" Module to handle errors on invalid files, permissions or workspace """

class OnSave:
    """ Check for syntax errors on file save """
    def __init__(self):
        pass # REMIND: init required variables

class OnFileRead:
    """ Check file errors, else return file """
    def __init__(self):
        pass # REMIND: init required variables
    try:
        # REMIND: Read file from user input (file selection).
        pass
    except PermissionError:
        print("File exists, but you lack permission to read it.")
    except TypeError:
        print("Invalid file type (unreadable file)!")
