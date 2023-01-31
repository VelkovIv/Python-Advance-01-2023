import os

try:
    file_path = 'my_first_file.txt'
    os.remove(file_path)

except FileNotFoundError as er:
    print("File already deleted!")