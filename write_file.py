def write_file(converted_file, save_path):
    """
    Write the file.
    """
    # Take the file name from the save path
    save_path = save_path.name

    print("Saving file to: " + save_path)
    with open(r""+save_path, "w") as file:
        file.write(converted_file)
    print("File written to: " + save_path)
    return save_path
