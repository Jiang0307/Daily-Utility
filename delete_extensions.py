"""
將delete_extensions.py所在資料夾開始，向下遞迴刪除輸入的檔案類型
"""
import os
from pathlib import Path

def input_extensions():
    extensions = []
    while True:
        line = str( input("Type extension to be removed : ") ).rstrip()
        if line == "":
            print("\nStart deleting...")
            break
        else:
            extensions.append("."+line)
    return extensions

def remove(path , extensions):
    for root, dirs, files in os.walk(path):
        for file in files:
            for ext in extensions:
                if (file.endswith(ext)):
                    path = Path(root).joinpath(file).as_posix()
                    if (Path(__file__).as_posix() != path):
                        print("delete : ",path)
                        os.remove(path)
            
if __name__ == '__main__':
    path = Path(__file__).parent
    extensions = input_extensions()
    remove(path , extensions)