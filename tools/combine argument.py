import os
import numpy as np
import cv2
from tqdm import tqdm
import re

def get_name(s):
    return re.search("TRA_RO_\d{7}", s).group()

def image_write(path_A, path_B, path_AB):
    im_A = cv2.imread(path_A, 1) # python2: cv2.CV_LOAD_IMAGE_COLOR; python3: cv2.IMREAD_COLOR
    im_B = cv2.imread(path_B, 1) # python2: cv2.CV_LOAD_IMAGE_COLOR; python3: cv2.IMREAD_COLOR
    im_AB = np.concatenate([im_A, im_B], 1)
    cv2.imwrite(path_AB, im_AB)

path_label = "Training dataset/SHARPEN//label_img"
path_img = "Training dataset/SHARPEN/img"
path_AB = "pub_test_ro"
img_list = os.listdir(path_img)


for img in tqdm(img_list):
    # print(get_name(img))
    # break
    # name_A = get_name(img)+'.png'
    name_A = img
    img_path_A = os.path.join(path_label, name_A)
    name_B = img
    img_path_B = os.path.join(path_img, name_B)
    name_AB = img[:len(img)-4] + '_bright.jpg'
    img_path_AB = os.path.join(path_AB, name_AB)
    image_write(img_path_A, img_path_B, img_path_AB)
