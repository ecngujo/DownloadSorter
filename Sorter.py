# Random project! 3/11/2026

import os
import shutil
import getpass
import platform
import sys

os_username = getpass.getuser()
os_name = platform.system() ## For future use?

# Default properties only! May not work with modified downloads location
root = os.path.join("C:\\Users", os_username)
downloads_folder = os.path.join(root, "Downloads")
desktop_folder = os.path.join(root, "Desktop")

# Storage for the category files
container_folder = os.path.join(desktop_folder, "Container")

if not os.path.isdir(downloads_folder):
  print("Download folder not found!")
  sys.exit()

categories = ["mp3", "mp4", "pdf", "docx", "png", "jpg"]

for category in categories:
  if not os.path.isdir(container_folder):
    os.mkdir(container_folder)

  location = os.path.join(container_folder, category)
  if not os.path.isdir(location):
    os.mkdir(location)


