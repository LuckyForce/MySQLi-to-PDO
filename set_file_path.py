from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import asksaveasfile

def set_file_path(file_path):
    """
    Get the file path from the user.
    """
    # Get the file name from the file path
    file_name = file_path.split("/")[-1]
    # Get the file name without the extension
    file_name_no_ext = file_name.split(".")[0]
    # New File Path
    new_file_path = file_path.replace(file_name, file_name_no_ext + "_converted.php")

    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = asksaveasfile(initialfile = new_file_path) # show an "Open" dialog box and return the path to the selected file
    return filename

