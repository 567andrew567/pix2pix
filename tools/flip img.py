import os
import cv2
from tqdm import tqdm

def flip_img(img_path):
    for i in tqdm(os.listdir(img_path)):
        if i.endswith('.jpg'):
            img = cv2.imread(img_path + i)
            img = cv2.flip(img, 0)
            cv2.imwrite(img_path + i.split('.')[0] + '_flip.jpg', img)

img_path = 'datasets/pub_ro/'

flip_img(f"{img_path}train/")
flip_img(f"{img_path}val/")