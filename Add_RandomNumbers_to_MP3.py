import os
import random
import sys

def rename_files_in_directory(directory='.'):
    """
    Renames all files in the specified directory by prefixing them with a random number,
    unless the file name already starts with '00'.
    
    :param directory: The path to the directory containing the files. Defaults to the current directory.
    """
    if not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    try:
        # List all files in the directory
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            
            # Skip if not a file
            if not os.path.isfile(file_path):
                continue
            
            # Skip files that start with "00"
            if file_name.startswith("00"):
                print(f"Skipping file: {file_name}")
                continue
            
            # Generate a random number between 1000 and 9999
            random_number = random.randint(100, 999)
            
            # Create the new file name
            new_file_name = f"{random_number}_{file_name}"
            new_file_path = os.path.join(directory, new_file_name)
            
            # Rename the file
            os.rename(file_path, new_file_path)
            print(f"Renamed: {file_name} -> {new_file_name}")
        
        print(f"Files renamed successfully in the directory: {directory}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get the directory from the command-line argument, or use the current directory
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    rename_files_in_directory(directory)
