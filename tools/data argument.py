import Augmentor
import cv2
import os

def get_img(path):
    res :list = []
    for i in os.listdir(path):
        if i.endswith('.jpg') or i.endswith('.png'):
            img = cv2.imread(os.path.join(path, i))
            res.append(img)

    return res

imgs = get_img("pub_argument")
augmentor = Augmentor.DataPipeline(imgs,os.listdir("pub_argument/label"))
# imgs.random_brightness(probability=0.5, min_factor=0.5, max_factor=1.3)
# augmentor.rotate(probability=0.7, max_left_rotation=0, max_right_rotation=0)
augmentor.sample(100)