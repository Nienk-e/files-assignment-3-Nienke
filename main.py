__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil
from zipfile import ZipFile
cwd = os.getcwd()
zip_file_path = os.path.join(cwd,"data.zip") 
cache_dir_path = os.path.join(cwd,"cache")

def clean_cache():
    cache_path = os.path.join(cwd, "cache")
    if 'cache' in os.listdir(cwd):
        shutil.rmtree(cache_path)
    if 'cache' not in os.listdir(cwd):
        os.mkdir('cache')
print(clean_cache())
        
def cache_zip(zip_file_path, cache_dir_path):
    with ZipFile(zip_file_path, 'r') as zip:
        zip.extractall(cache_dir_path)
print (cache_zip(zip_file_path, cache_dir_path))

def cached_files():
    cached_files_list = [
        os.path.abspath(os.path.join(cwd, "cache", file_path)) for file_path in os.listdir(cache_dir_path)
        ]
    return cached_files_list

def find_password(cached_files):
    for file_name in cached_files:
        with open(file_name, "r") as file:
            for line in file.readlines():
                if "password" in line:
                    password_line = (line.split(": ")[1]).rstrip("\n")
    return password_line

print(f'The password is: {find_password(cached_files())}')
