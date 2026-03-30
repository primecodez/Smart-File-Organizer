import os
import shutil

# Path to organize (change this)
SOURCE_FOLDER = "test_folder"

# File type mapping
FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"]
}

def organize_files():
    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)

        if os.path.isfile(file_path):
            for folder, extensions in FILE_TYPES.items():
                if any(file.endswith(ext) for ext in extensions):
                    
                    target_folder = os.path.join(SOURCE_FOLDER, folder)
                    os.makedirs(target_folder, exist_ok=True)

                    shutil.move(file_path, os.path.join(target_folder, file))
                    print(f"Moved: {file} → {folder}")

organize_files()