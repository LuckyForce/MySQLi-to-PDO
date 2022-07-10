# Main File

# Imports
from get_file_path import get_file_path
from read_file import read_file
from convert_file import convert_file
from set_file_path import set_file_path
from write_file import write_file

# Main Method
def main():
    print("MySQLi-to-PDO")
    # Read in the file with a file chooser
    file_path = get_file_path()
    # Read in the file
    file_contents = read_file(file_path)
    # Convert the file
    converted_file = convert_file(file_contents)
    # Read in the path to save the file
    save_path = set_file_path(file_path)
    # Write the file
    write_file(converted_file, save_path)


if __name__ == "__main__":
    main()