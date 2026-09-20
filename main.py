import os
import shutil

# Folder where files are placed
SOURCE_FOLDER = "test_files"

# File categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"]
}


def get_category(file_extension):
    """Return the category for a given file extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category

    return "Others"


def organize_files():
    """Organize files into folders based on their extensions."""

    if not os.path.exists(SOURCE_FOLDER):
        print("Error: test_files folder not found.")
        return

    files_moved = 0

    for file_name in os.listdir(SOURCE_FOLDER):

        file_path = os.path.join(SOURCE_FOLDER, file_name)

        # Ignore folders
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, extension = os.path.splitext(file_name)

        # Find category
        category = get_category(extension)

        # Create category folder automatically
        category_folder = os.path.join(SOURCE_FOLDER, category)
        os.makedirs(category_folder, exist_ok=True)

        # Move file
        destination = os.path.join(category_folder, file_name)

        try:
            shutil.move(file_path, destination)
            print(f"Moved: {file_name} → {category}/")
            files_moved += 1

        except shutil.Error:
            print(f"Could not move: {file_name}")

    print("\n--------------------------------")
    print("File organization completed!")
    print(f"Total files moved: {files_moved}")
    print("--------------------------------")


if __name__ == "__main__":
    organize_files()