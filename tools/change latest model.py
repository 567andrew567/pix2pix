import os
import shutil
import sys


if __name__ == "__main__":
    if(len(sys.argv) != 4):
        raise Exception("python change_latest_model.py <model_path> <model_name> <save_path>")

    # get args
    model_path = sys.argv[1]
    model_name = sys.argv[2]
    save_path = sys.argv[3]
    print(f"{model_path=}")
    print(f"{model_name=}")
    print(f"{save_path=}")
    # model_path = 'checkpoints/pub/'
    # model_name = '300_net_G.pth'

    if os.path.exists(model_path + model_name):
        shutil.copy(os.path.join(model_path,model_name), f"{save_path}/latest_net_G.pth")
    else:
        raise Exception(f"{os.path.join(model_path,model_name)} is not exist")
