import os

def rename_file_with_text(filename, output_directory):
    # Get the file's directory and name without the extension
    filename = os.path.basename(filename)
    # Create the new filename by appending text
    new_filename = output_directory + "/"+ filename
    
    # Rename the file
    
    return new_filename

# Example usage
old_filename = "example.txt"
output_directory = "/Users/vishnuagrawal/Desktop/Project/data/outputImages"
new_filename = rename_file_with_text(old_filename, output_directory)
print(f"File renamed to: {new_filename}")