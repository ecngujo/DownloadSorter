# Random project! 3/11/2026

import os
import shutil
import getpass
import platform
import sys
from pathlib import Path

# Just for prints :D
debug = True

os_username = getpass.getuser()
os_name = platform.system() ## For future use?

# Default properties only! May not work with modified downloads location
root = os.path.join("C:\\Users", os_username)
downloads_folder = os.path.join(root, "Downloads")
desktop_folder = os.path.join(root, "Desktop")

if not os.path.isdir(downloads_folder):
  print("Download folder not found!")
  sys.exit()


# Storage for the category files
container_folder = os.path.join(desktop_folder, "Container")
if not os.path.isdir(container_folder):
    os.mkdir(container_folder)


categories = ["mp3", "mp4", "pdf", "docx", "png", "jpg", "exe", "zip", "pptx"]

# Check if the categories exists in the container, if not then create
for category in categories:
  location = os.path.join(container_folder, category)
  if not os.path.isdir(location):
    os.mkdir(location)
    print(f"Created {category} in {container_folder}!")

# Sorting

filesSorted = 0
for file in os.listdir(downloads_folder):
  file_location = os.path.join(downloads_folder, file)
  if not os.path.isdir(file_location):
    for category in categories:
      category_location = os.path.join(container_folder, category)
      if Path(file).suffix == f".{category}":
        shutil.move(file_location, category_location)
        if debug == True:
          print(f"Moved {file[0:5]}..{Path(file).suffix} -> {category}!")
        filesSorted += 1
# I think this is pretty bad algorithm, it's a nested for loop. Not viable for larger files. I will refactor this

print(f"Total files sorted: {filesSorted}")