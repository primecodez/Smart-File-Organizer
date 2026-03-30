import os
import shutil

SOURCE_FOLDER = "test_folder"

# Rule 1: Keyword-based (SMART RULES)
KEYWORD_RULES = {
    "invoice": "Finance",
    "resume": "Career",
    "assignment": "Study"
}

# Rule 2: Extension-based (fallback)
FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"]
}

def organize_files():
    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)

        if os.path.isfile(file_path):
            file_lower = file.lower()
            moved = False   # to track if file is already moved

            # 🔥 STEP 1: Check keyword rules FIRST
            for keyword, folder in KEYWORD_RULES.items():
                if keyword in file_lower:
                    move_file(file_path, file, folder)
                    moved = True
                    break   # stop checking further

            # 🔥 STEP 2: If no keyword matched → use extension
            if not moved:
                for folder, extensions in FILE_TYPES.items():
                    if any(file_lower.endswith(ext) for ext in extensions):
                        move_file(file_path, file, folder)
                        break

def move_file(file_path, file, folder):
    target_folder = os.path.join(SOURCE_FOLDER, folder)
    os.makedirs(target_folder, exist_ok=True)

    destination = os.path.join(target_folder, file)
    shutil.move(file_path, destination)

    print(f"Moved: {file} → {folder}")

organize_files()