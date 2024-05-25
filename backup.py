import os
import shutil
import tarfile
import zipfile
import platform

DIRS_NAME = input("ENTER LOCATION OF DIRECTORIE YOU WANT TO BACKUP SEPARATED BY A SPACE : ")
DIRS_LOCATION = DIRS_NAME.split()
current_platform = platform.system()

if current_platform == "Windows":
    for item in DIRS_LOCATION:
      shutil.copytree(item, os.path.basename(item))
    with zipfile.ZipFile("backup.zip", "w", compression=zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk("."):
            for file in files:
                zipf.write(os.path.join(root, file))
elif current_platform == "Linux":
    backup_name = "backup.tar.gz"
    with tarfile.open(backup_name, "w:gz") as tar:
        for item in DIRS_LOCATION:
            tar.add(item)
    



