# Step 1: File Creation
def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("Line 1: Hello, this is the first line.\n")
            file.write("Line 2: The number is 12345.\n")
            file.write("Line 3: Python file handling example.\n")
        print("File 'my_file.txt' created and written successfully.")
    except PermissionError:
        print("You do not have permission to write to this file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File creation operation completed.")


# Step 2: Read and Display File Contents
def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("Reading 'my_file.txt':")
            print(content)
    except FileNotFoundError:
        print("File not found. Please ensure 'my_file.txt' exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File reading operation completed.")


# Step 3: Append Text to the File
def append_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("Line 4: Appending new text to the file.\n")
            file.write("Line 5: Another appended line with 67890.\n")
            file.write("Line 6: File handling in Python is fun!\n")
        print("Text appended to 'my_file.txt' successfully.")
    except PermissionError:
        print("You do not have permission to write to this file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File append operation completed.")


# Main execution
if __name__ == "__main__":
    create_file()  # Create and write to the file
    read_file()    # Read the file
    append_file()  # Append text to the file
    read_file()    # Read the file again to display new content
