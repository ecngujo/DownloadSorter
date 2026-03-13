# Random project! 3/11/2026

import os
import shutil
import getpass
import platform
import sys

os_username = getpass.getuser()
os_name = platform.system() ## For future use?

# Default properties only! May not work with modified downloads location\
downloads_folder = f"C:\\Users\\{os_username}\\Downloads"

if not os.path.isdir(downloads_folder):
  print("Download folder not found!")
  sys.exit()

categories = ["mp3", "mp4", "pdf", "docx", "png", "jpg"]


