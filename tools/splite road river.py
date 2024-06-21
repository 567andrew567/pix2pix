import os

path = "pub"
path_ri = "pub_ri"
path_ro = "pub_ro"

img_list = os.listdir(path)

for img in img_list:
    if img.find("RI") != -1:
        os.rename(os.path.join(path, img), os.path.join(path_ri, img))
    else:
        os.rename(os.path.join(path, img), os.path.join(path_ro, img))