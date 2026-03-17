# Random project! 3/11/2026

import shutil
import getpass
import sys
from pathlib import Path

os_username = getpass.getuser()

excluded = ["c", "ico", "png"]

# Default properties only! May not work with modified downloads location :P
root = Path("C:/") / "Users" / os_username
downloads_folder = Path(root) / "Downloads"
desktop_folder = Path(root) / "Desktop"
container_folder = Path(desktop_folder) / "Container"

if not downloads_folder.is_dir():
  print("Downloads folder not found!")
  sys.exit()

# Storage for the category folders
if not container_folder.is_dir():
  print("Creating container..")
  Path(container_folder).mkdir()

for file in downloads_folder.iterdir():
  fileSuffix = file.suffix.replace(".", "")
  if file.is_file() and str(fileSuffix) not in excluded:
    try:
      folder = Path(downloads_folder) / fileSuffix
      folder.mkdir(exist_ok=True)
      shutil.move(str(file), str(Path(folder) / file.name))
      print(f"{file.name[0:5]}.. -> {folder}")
    except FileNotFoundError:
      print(f"{file.name} not found or doesn't exist!")
    except Exception as e:
      print(f"Error found: {e}")