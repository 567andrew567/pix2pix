import os
import numpy as np
import cv2
from tqdm import tqdm


def image_write(path_A, path_B, path_AB):
    im_A = cv2.imread(path_A, 1) # python2: cv2.CV_LOAD_IMAGE_COLOR; python3: cv2.IMREAD_COLOR
    im_B = cv2.imread(path_B, 1) # python2: cv2.CV_LOAD_IMAGE_COLOR; python3: cv2.IMREAD_COLOR
    im_AB = np.concatenate([im_A, im_B], 1)
    cv2.imwrite(path_AB, im_AB)

path_A = "34_Competition_1_public_testing_dataset/label_img"
path_B = "34_Competition_1_Training_dataset/Training_dataset/img"
path_AB = "pub_test"
img_list = os.listdir(path_A)
no_b = True

for img in tqdm(img_list):
    name_A = img
    img_path_A = os.path.join(path_A, name_A)
    name_B = img
    img_path_B = os.path.join(path_B, name_B)
    if no_b:
        img_path_B = "imgs/black.png"
    name_AB = img.replace(".png", ".jpg")
    img_path_AB = os.path.join(path_AB, name_AB)
    image_write(img_path_A, img_path_B, img_path_AB)
