import os
import shutil

path = "/Users/arth/Downloads/dtd/images"
dest = "/Users/arth/Desktop/"

if not os.path.exists(os.path.join(dest, "backgroud_ds")):
    os.mkdir(os.path.join(dest, "backgroud_ds"))

for dirs in os.listdir(path):
    if not(dirs.startswith('.')):
        dir_path = os.path.join(path, dirs)
        for i, subdirs in enumerate(os.listdir(dir_path)):
            image_path = os.path.join(dir_path, subdirs)
            if(i <= 20):
                shutil.copy(image_path, os.path.join(dest, "backgroud_ds"))
            else:
                break
