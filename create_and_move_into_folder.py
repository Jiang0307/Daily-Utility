"""
將資料夾中所有檔案分別建立並移至該資料夾
"""
import os
import shutil  
from pathlib import Path

black_list = [".git" , ".gitignore" , "README.md"]

def create_and_move_into_folder():
    parent_dir = Path(__file__).parent.absolute()
    files = os.listdir(parent_dir)
    for file in files:
        file_name = Path(parent_dir).joinpath(file).as_posix()
        if file_name != Path(__file__).as_posix():
            print(file_name)
            stop = False
            for extension in black_list:
                if (file.endswith(extension)):
                    stop = True
            if stop == False:
                folder_name = Path(file).resolve().stem
                folder_path = Path(parent_dir).joinpath(folder_name).as_posix()
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)
                shutil.move(file_name , folder_path )

if __name__ == '__main__':
    create_and_move_into_folder()