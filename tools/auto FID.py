import subprocess
import os
from functools import cmp_to_key
from subprocess import PIPE, run

def path_cmp(path1, path2):
    return len(path1) - len(path2)


def run_cmd(cmd_str,re_res=False):
    print(f"run cmd: {cmd_str}")
    res = run(cmd_str, shell=True, stdout=PIPE)
    return res.stdout.replace(b'\n', b'').decode('ascii').replace('[0m','') if re_res else None

model_path = 'checkpoints/pub_ro/'

G_model_filter: filter = filter(lambda x: x.endswith('G.pth') and not 'latest' in x, os.listdir(model_path))
model_list = sorted(list(G_model_filter), key=cmp_to_key(path_cmp))
print(model_list)
with open('FID_res.txt', 'w') as f:
    for model in model_list[150:200]:
        print(f"copy {model} to latest_net_G.pth")
        run_cmd(f'python "change latest model.py" {model_path} {model} {model_path}')
        print(f"run test {model}")
        run_cmd(f'python test.py --dataroot ./datasets/pub_ro --name pub_ro --model pix2pix --direction AtoB --eval')
        print(f"run create FID file")
        run_cmd(f'python "FID.py" pub_ro')
        print(f"calulate FID")
        fid_res = run_cmd('python -m pytorch_fid FID/real FID/fake', re_res=True)
        print(f"fid_res: {fid_res}")
        # out put res to file
        f.write(f"{model}\n{fid_res}\n")


