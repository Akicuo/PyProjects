import os
import shutil
from tqdm import tqdm

DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")

FILE_TYPES = {
    "Text Files": [".txt"],
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".apng", ".avif", ".bmp", ".ico", ".tifff"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".avchd"],
    "Documents": [".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code Files": [".py", ".java", ".cpp", ".c", ".html", ".css", ".js"],
    "Music": [".mp3", ".wav", ".flac"]
}

def create_directories():
    for folder_name in FILE_TYPES:
        folder_path = os.path.join(DOWNLOADS_FOLDER, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def organize_files():
    files = [f for f in os.listdir(DOWNLOADS_FOLDER) if os.path.isfile(os.path.join(DOWNLOADS_FOLDER, f))]

    for filename in tqdm(files, desc="Organizing files", unit="file"):
        file_path = os.path.join(DOWNLOADS_FOLDER, filename)
        
        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(filename)[1].lower()
        moved = False

        for folder_name, extensions in FILE_TYPES.items():
            if file_extension in extensions:
                dest_folder = os.path.join(DOWNLOADS_FOLDER, folder_name)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                moved = True
                break

        if not moved:
            other_folder = os.path.join(DOWNLOADS_FOLDER, "Others")
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(file_path, os.path.join(other_folder, filename))

if __name__ == "__main__":
    create_directories()
    organize_files()
    print("Download folder organized successfully!")
