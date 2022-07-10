def convert_connection_string(file_contents):
    """
    Convert the connection string.
    """
    # MySQLi Variant from https://www.w3schools.com/php/php_mysql_connect.asp
    # // Create connection
    # $conn = new mysqli($servername, $username, $password, $dbname);

    # // Check connection
    # if ($conn->connect_error) {
    # die("Connection failed: " . $conn->connect_error);
    # }
    # echo "Connected successfully";
    # PDO Variant from https://www.w3schools.com/php/php_mysql_connect.asp
    #     try {
    #   $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    #   // set the PDO error mode to exception
    #   $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    #   echo "Connected successfully";
    # } catch(PDOException $e) {
    #   echo "Connection failed: " . $e->getMessage();
    # }
    # Replace MySQLi with PDO
    converted_file = file_contents.replace("new mysqli(", "new PDO(")
    # Replace the connection string
    # Get the connection string
    connection_string_start = converted_file.find("new PDO(")
    connection_string_end = converted_file.find(")", connection_string_start)
    if connection_string_start == -1 or connection_string_end == -1:
        print("Info: No connection string found.")
        return converted_file
    connection_string = converted_file[connection_string_start+len("new PDO("):connection_string_end]
    # Take the connection string and take it apart
    connection_string_parts = connection_string.split(",")
    # Trim the parts
    connection_string_parts = [part.strip() for part in connection_string_parts]
    # Create the new connection string
    new_connection_string = "\"mysql:host=" + connection_string_parts[0] + ";dbname=" + connection_string_parts[3] + "\", " + connection_string_parts[2] + ", " + connection_string_parts[1]
    # Replace the connection string
    converted_file = converted_file.replace(connection_string, new_connection_string)

    # TODO: Add try catch block for the connection string, change Attributes for PDO and change error check
    
    return converted_file