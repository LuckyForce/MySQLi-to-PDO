def convert_file(file_contents):
    """
    Convert the file.
    """
    # Replace MySQLi with PDO
    converted_file = file_contents.replace("MySQLi", "PDO")
    return converted_file