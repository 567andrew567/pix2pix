import Augmentor
import os
import shutil
from tqdm import tqdm
import cv2


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)


def datastrength(data_path, out, num):
    p = Augmentor.Pipeline(data_path, output_directory=out, save_format='png')
    p.random_brightness(probability=0.5, min_factor=0.5, max_factor=1.3)
    # p.rotate90(probability=1)  # 逆时针随机旋转90度（随机概率可自行设定）
    # p.rotate270(probability=1)  # 顺时针随机旋转90度（随机概率可自行设定）
    # p.rotate(probability=1, max_left_rotation=25, max_right_rotation=25)  # 不固定角度微小旋转：比如向左最大旋转25度，向右最大旋转10度(备注：旋转最大角度范围是0-25度)
    # p.skew_tilt(probability=1, magnitude=1)  # 透视形变-垂直方向形变：magnitude取（0,1），指的是形变程度
    # p.skew_corner(probability=1, magnitude=1)  # 透视形变-斜四角形变形变：magnitude取（0,1），指的是形变程度
    # p.random_distortion(probability=1, grid_height=5, grid_width=16, magnitude=8)  # 弹性扭曲，类似区域扭曲的感觉
    # p.shear(probability=1, max_shear_left=15, max_shear_right=15)  # 错切变换
    # p.random_erasing(probability=1, rectangle_area=0.5)  # 随机区域擦除
    p.sample(num)  # 生成n张这样操作的图片


def sharpen(img, sigma=100):
    # sigma = 5、15、25
    blur_img = cv2.GaussianBlur(img, (0, 0), sigma)
    usm = cv2.addWeighted(img, 1.5, blur_img, -0.5, 0)
    return usm


if __name__ == "__main__":
    SET_NUM = 4320
    # image
    IMG_PATH = r'.\Training dataset\Original\img'
    LABEL_IMG_PATH = r'.\Training dataset\Original\label_img'

    SHARPEN_PATH = r'.\Training dataset\SHARPEN'
    brightness_PATH = r'.\Training dataset\brightness'
    img_list = os.listdir(IMG_PATH)

    if os.path.exists(SHARPEN_PATH):
        shutil.rmtree(SHARPEN_PATH)
    mkdir(SHARPEN_PATH)
    mkdir(SHARPEN_PATH + '/img')
    mkdir(SHARPEN_PATH + '/label_img')
    for i in tqdm(img_list):
        buf = cv2.imread(IMG_PATH + '/' + i)
        buf2 = cv2.imread(LABEL_IMG_PATH + '/' + i.split('.')[0] + '.png')
        os.rename(IMG_PATH + '/' + i, IMG_PATH + '/' + i.split('.')[0] + '.png')
        output = sharpen(buf, 25)
        cv2.imwrite(SHARPEN_PATH + '/img/' + i.split('.')[0] + '_SHARPEN.png', output)
        cv2.imwrite(SHARPEN_PATH + '/label_img/' + i.split('.')[0] + '_SHARPEN.png', buf2)

    if os.path.exists(brightness_PATH):
        shutil.rmtree(brightness_PATH)
    mkdir(brightness_PATH)
    mkdir(brightness_PATH + '/img')
    mkdir(brightness_PATH + '/label_img')

    datastrength(IMG_PATH, '../../../' + brightness_PATH + '/img', SET_NUM)
    label_img_list = os.listdir(LABEL_IMG_PATH)
    new_img_list = os.listdir(brightness_PATH + '/img')
    for i in tqdm(new_img_list):
        for j in label_img_list:
            if j.split('.')[0] in i:
                buf = cv2.imread(LABEL_IMG_PATH + '/' + j)
                cv2.imwrite(brightness_PATH + '/label_img/' + i, buf)
