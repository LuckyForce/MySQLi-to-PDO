def read_file(file_path):
    """
    Read in the file.
    """
    with open(file_path, "r") as file:
        file_contents = file.read()
    return file_contents