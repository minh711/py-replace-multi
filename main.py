import os

def replace_text_in_file(file_path, old_text, new_text):
    # Read the file's contents
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()
    
    # Replace the old text with the new text and count replacements
    count = file_contents.count(old_text)
    new_contents = file_contents.replace(old_text, new_text)
    
    # Write the new contents back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_contents)
    
    return count

def replace_text_in_files(folder_path, old_text, new_text, file_extension):
    print("Program started")
    total_replacements = 0
    
    # Iterate over all files in the specified folder
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(file_extension):
                file_path = os.path.join(root, file_name)
                try:
                    count = replace_text_in_file(file_path, old_text, new_text)
                    total_replacements += count
                    print(f'Replaced {count} occurrences in file: {file_path}')
                except UnicodeDecodeError:
                    print(f'Skipping file due to decoding error: {file_path}')
    
    print(f'Total replacements made: {total_replacements}')

def main():
    # Define parameters here
    folder_path = 'files'  # Change this to your folder path
    old_text = 'old text'
    new_text = 'new text'
    file_extension = ''  # Check all files regardless of extension

    # Replace text in files
    replace_text_in_files(folder_path, old_text, new_text, file_extension)

if __name__ == "__main__":
    main()
