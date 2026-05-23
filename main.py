import os
import shutil

# Folder path to organize
path = input("Enter folder path: ")

# File type categories
file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"],
    "Programs": [".py", ".java", ".cpp"]
}

# Organize files
for file in os.listdir(path):
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()

        for folder, extensions in file_types.items():
            if extension in extensions:

                folder_path = os.path.join(path, folder)

                # Create folder if not exists
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Move file
                shutil.move(file_path, os.path.join(folder_path, file))

                print(f"Moved: {file} -> {folder}")
                break

print("Files organized successfully!")