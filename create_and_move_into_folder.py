"""
將資料夾中所有檔案分別建立並移至該資料夾
"""
import os
import shutil  
from pathlib import Path

current_path = Path(__file__)
parent_dir = current_path.parent.absolute()
files = os.listdir(parent_dir)

for file in files:
    if (file.endswith(".git")) or (file.endswith(".gitignore")) or (file.endswith("README.md")):
        continue
    else:
        print(file)
        folder_name = Path(file).resolve().stem
        os.mkdir(Path(parent_dir).joinpath(folder_name))
        shutil.move(Path(parent_dir).joinpath(file).as_posix() , Path(parent_dir).joinpath(folder_name).as_posix() )