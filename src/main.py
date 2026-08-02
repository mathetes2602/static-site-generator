import os
import shutil

def copy_files(origin, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    os.mkdir(destination)
    dir_items = os.listdir(origin)
    for item in dir_items:
        item_path = os.path.join(origin, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, os.path.join(destination, item))
        if os.path.isdir(item_path):
            copy_files(item_path, os.path.join(destination, item))
    
def main():
    main_dir = os.path.abspath("./")
    public_path = os.path.join(main_dir, "public")
    static_path = os.path.join(main_dir, "static")
    copy_files(static_path, public_path)      
main()