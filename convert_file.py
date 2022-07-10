# Imports from converter folder
from converter.convert_connection_string import convert_connection_string
# from convert_query import convert_query
# from convert_prepare import convert_prepare
# from convert_execute import convert_execute
# from convert_fetch import convert_fetch
# from convert_fetch_all import convert_fetch_all
# from convert_fetch_assoc import convert_fetch_assoc
# from convert_fetch_array import convert_fetch_array
# from convert_fetch_object import convert_fetch_object
# from convert_fetch_row import convert_fetch_row
# from convert_fetch_field import convert_fetch_field
# from convert_fetch_field_direct import convert_fetch_field_direct
# from convert_fetch_field_directs import convert_fetch_field_directs
# from convert_fetch_fields import convert_fetch_fields
# from convert_fetch_lengths import convert_fetch_lengths



def convert_file(file_contents):
    """
    Convert the file.
    """
    # Replace MySQLi with PDO
    # converted_file = file_contents.replace("MySQLi", "PDO")
    converted_file = file_contents
    converted_file = convert_connection_string(converted_file)
    # converted_file = convert_query(converted_file)
    # converted_file = convert_prepare(converted_file)
    # converted_file = convert_execute(converted_file)
    # converted_file = convert_fetch(converted_file)
    # converted_file = convert_fetch_all(converted_file)
    # converted_file = convert_fetch_assoc(converted_file)
    # converted_file = convert_fetch_array(converted_file)
    # converted_file = convert_fetch_object(converted_file)
    # converted_file = convert_fetch_row(converted_file)
    # converted_file = convert_fetch_field(converted_file)
    # converted_file = convert_fetch_field_direct(converted_file)
    # converted_file = convert_fetch_fields(converted_file)
    # converted_file = convert_fetch_lengths(converted_file)
    # converted_file = convert_fetch_field_directs(converted_file)

    return converted_file