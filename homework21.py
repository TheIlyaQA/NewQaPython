import os

def process_directory(directory_path, output_file):
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            if filename.endswith('.txt'):
                file_path = os.path.join(dirpath, filename)
                if os.path.getsize(file_path) <= 120:
                    with open(file_path, 'r') as file:
                        content = file.read()
                        output_file.write(f"Filename: {filename}\nContent: {content}\n\n")

source_directory = "your/source/directory/path"
with open("combined_files.txt", "w") as combined_file:
    process_directory(source_directory, combined_file)
