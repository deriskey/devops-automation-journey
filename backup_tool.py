import os
import shutil
from datetime import datetime

# Get current date & time
current_time = datetime.now().strftime("%Y-%m-%d_%H%M%S")

#define source directory 
source_dir = "live_data"

#Define a unique backup destination folder name using the timestamp
destination_dir = f"backup_{current_time}"

print(f"Starting backup process for: '{source_dir}'...")

#check source directory actually exists before copying
if os.path.exists(source_dir):
    #shutil.copytree copies an entire folder and everything inside it
    shutil.copytree(source_dir, destination_dir)
    print("Backup complted succesccfully!")
    print(f" New archive folder created: '{destination_dir}'")
else:
    print(f"X Error: The sourcecfolder '{source_dir}'does not exist.")