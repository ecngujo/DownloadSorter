# Random project! 3/11/2026

import shutil
import getpass
import sys
from pathlib import Path

os_username = getpass.getuser()

# Default settings for me
excluded = ["c", "ico", "png", "py", "lua", "jpg", "webp", "exe"]

# Default properties only! May not work with modified downloads location :P
root = Path("C:/") / "Users" / os_username
downloads_folder = Path(root) / "Downloads"
desktop_folder = Path(root) / "Desktop"

if not downloads_folder.is_dir():
  print("Downloads folder not found!")
  sys.exit()

totalFiles = 0
for file in downloads_folder.iterdir():
  fileSuffix = file.suffix.replace(".", "").lower()
  if file.is_file() and str(fileSuffix) not in excluded:
    try:
      folder = Path(downloads_folder) / fileSuffix
      folder.mkdir(exist_ok=True)
      #shutil.move(str(file), str(Path(folder) / file.name))
      totalFiles = totalFiles + 1
      print(f"{file.name[0:9]}.. -> {folder}")
    except FileNotFoundError:
      print(f"{file.name} not found or doesn't exist!")
    except Exception as e:
      print(f"Error found: {e}")

print(f"{totalFiles} files has been moved")