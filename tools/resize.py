import os
import cv2
from tqdm import tqdm


img_paths = ["upload_ri", "upload_ro"]
save_path = "upload resize"
if not os.path.exists(save_path):
    os.makedirs(save_path)
for img_path in img_paths:
    print(len(os.listdir(img_path)))
    for i in tqdm(os.listdir(img_path)):
        img = cv2.imread(f"{img_path}/{i}")
        img = cv2.resize(img, (428, 240),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(f"{save_path}/{i}", img)