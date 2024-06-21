import os
import random

path = "pub_ro"
sava_path = "datasets\pub_ro"

train_num  = 1728
val_num = 216
test_num = 216

img_list = os.listdir(path)
random.seed(1024)
random.shuffle(img_list)

train_list = img_list[:train_num]
val_list = img_list[train_num:train_num+val_num]
test_list = img_list[train_num+val_num:]

for i in train_list:
    os.rename(os.path.join(path, i), os.path.join(f"{sava_path}/train", i))

for i in val_list:
    os.rename(os.path.join(path, i), os.path.join(f"{sava_path}/val", i))

for i in test_list:
    os.rename(os.path.join(path, i), os.path.join(f"{sava_path}/test", i))