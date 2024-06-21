import os
import shutil
import sys
from tqdm import tqdm

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise Exception("python FID.py <result_path>")

    result_path = sys.argv[1]
    print(f"{result_path=}")
    res_path = f"results/{result_path}/test_latest/images/"

    if os.path.exists('FID'):
        shutil.rmtree('FID')
    os.makedirs('FID')
    os.makedirs('FID/real')
    os.makedirs('FID/fake')


    for i in tqdm(os.listdir(res_path)):
        if 'TRA' in i:
            if 'fake' in i:
                shutil.copy(res_path+i, 'FID/fake/'+i.replace('_fake_B',''))
            elif 'real_B' in i:
                shutil.copy(res_path+i, 'FID/real/'+i.replace('_real_A',''))
