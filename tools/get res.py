import os
import shutil
import cv2
from tqdm import tqdm

res_path = 'results/pub/test_latest/images/'
save_path = 'upload/'
img_list = os.listdir(res_path)

if os.path.exists(save_path):
    shutil.rmtree(save_path)
os.makedirs(save_path)

for i in tqdm(img_list):
    if i.endswith('.png') and 'fake' in i and ('PUB' in i or 'PRI' in i):
        img = cv2.imread(res_path + i)
        cv2.imwrite(save_path + i.replace('_fake_B','').replace('png','jpg'), img)