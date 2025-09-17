# #Secindary Storage
# #opening a file - file handle
# #Open the file using open()
#
# Use the open() Open the file using open()
#
# Use the open() function to open the file.
# Syntax: file = open("filename", "mode")
# Common modes:
# 'r' for reading (default).
# 'rb' for reading in binary.
# Read the file content
#
# Use methods like .read(), .readline(), or .readlines() depending on how you want to process the file:
# .read() reads the entire file as a string.
# .readline() reads one line at a time.
# .readlines() reads all lines into a list.
# Process the file content
#
# Store or manipulate the content as needed.
# Example: Use a loop to process lines in a file for large data.
# Close the file using close()
#
# Use the .close() method to release system resources.
# Use with for safer file handling (Recommended)
#
# Using a with statement automatically closes the file, even if an error occurs.
with open("filename", "r") as file:
    content = file.read()
# What to Remember:
# File Modes: Always specify the correct mode ('r', 'w', 'a', 'rb', etc.) based on your requirement.
# Error Handling: Handle exceptions using try...except blocks to avoid runtime errors (e.g., file not found).
# Use with: Always prefer with to avoid forgetting to close the file, which could lead to resource leaks.
# File Path: Use the correct file path. For relative paths, ensure the script's directory matches the file location.
# Encoding: For text files, use the appropriate encoding (open("filename", "r", encoding="utf-8")) to avoid issues with special characters.

# Step 1: Use the 'with' statement to open the file
with open("example.txt", "r", encoding="utf-8") as file:
    # Step 2: Read the content of the file
    content = file.read()

    # Step 3: Process the content (e.g., print or analyze)
    print("File Content:")
    print(content)

# Note: The file is automatically closed after the 'with' block

# Line-by-Line Reading Example
# If the file is large, you can read it line by line to save memory:

# Open and read the file line by line
with open("example.txt", "r", encoding="utf-8") as file:
    print("Reading file line by line:")
    for line in file:
        print(line.strip())  # Remove trailing newline characters

# Error Handling Example
# To handle errors (e.g., file not found):

try:
    with open("example.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print("File Content:")
        print(content)
except FileNotFoundError:
    print("Error: The file 'example.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")