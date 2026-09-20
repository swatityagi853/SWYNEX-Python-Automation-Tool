# SWYNEX Python Automation Tool

## 📌 Project Overview

The SWYNEX Python Automation Tool is a simple file organization automation system developed using Python.

The tool automatically organizes files into separate folders according to their file extensions. This reduces manual effort and makes file management faster and easier.

## ✨ Features

- Automatically detects file extensions
- Organizes files into appropriate categories
- Creates category folders automatically
- Supports images, documents, videos, audio, spreadsheets and archives
- Places unknown file types into an "Others" folder
- Displays the files moved in the terminal
- Shows the total number of files processed

## 🛠️ Technologies Used

- Python 3
- `os` module
- `shutil` module

## 📂 Project Structure

```text
SWYNEX-Python-Automation-Tool/
│
├── main.py
├── README.md
├── requirements.txt
│
└── test_files/
## 📁 File Categories

| Category | Supported Extensions |
|----------|----------------------|
| Images | .jpg, .jpeg, .png, .gif, .webp |
| Documents | .pdf, .doc, .docx, .txt |
| Videos | .mp4, .mkv, .avi, .mov |
| Audio | .mp3, .wav, .aac, .flac |
| Spreadsheets | .xls, .xlsx, .csv |
| Archives | .zip, .rar, .7z, .tar, .gz |
| Others | Other file types |

## ⚙️ How It Works

1. The program checks the `test_files` folder.
2. It reads each file present in the folder.
3. It identifies the file extension.
4. It determines the appropriate category.
5. The required category folder is created automatically.
6. The file is moved into the corresponding folder.
7. The program displays the result in the terminal.
8. Finally, it displays the total number of files moved.

## ▶️ How to Run

### Step 1: Open the project

Open the project folder in Visual Studio Code.

### Step 2: Add files

Place files that you want to organize inside:

```text
test_files/
### Step 3: Run the program

Open the terminal in VS Code and run:

```bash
python main.py
```

### Step 4: Check the result

The program will automatically create category folders inside `test_files/` and move files according to their extensions.

Example:

```text
test_files/
├── Images/
├── Documents/
├── Videos/
├── Audio/
├── Spreadsheets/
├── Archives/
└── Others/
```

### Example Output

```text
Moved: photo.jpg → Images/
Moved: resume.pdf → Documents/
Moved: song.mp3 → Audio/
Moved: video.mp4 → Videos/

--------------------------------
File organization completed!
Total files moved: 4
--------------------------------
```

## 🎯 Purpose

This project demonstrates how Python can be used to automate repetitive file management tasks and reduce manual effort.