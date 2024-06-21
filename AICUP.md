## train

### train
test dataset
`python train.py --dataroot ./datasets/ROAD_pix2pix --name ROAD_pix2pix --model pix2pix --direction AtoB`

pub RI dataset
`
python train.py 
--dataroot ./datasets/pub 
--name pub 
--model pix2pix 
--direction AtoB 
--save_latest_freq 1000 
--save_epoch_freq 10
--n_epochs 300
--n_epochs_decay 300
--batch_size 4
--lr 0.001
--lr_policy cosine
`
try lr 0.001 use cosine lr_policy epoch 200 epoch_decay 200

pub RO dataset
`
python train.py 
--dataroot ./datasets/pub_ro 
--name pub_ro 
--model pix2pix 
--direction AtoB 
--save_latest_freq 10000 
--save_epoch_freq 10
--n_epochs 1500 
--n_epochs_decay 500 
--batch_size 2
--lr 0.0004
--lr_policy step
--netG unet_256 
--continue_train
--epoch_count 1501
`

## test
test dataset
`python test.py --dataroot ./datasets/ROAD_pix2pix --name ROAD_pix2pix --model pix2pix --direction AtoB`

pub ri dataset
`
python test.py  
--dataroot ./datasets/pub 
--name pub 
--model pix2pix 
--direction AtoB
`

pub ro dataset
`
python test.py  
--dataroot ./datasets/pub_ro 
--name pub_ro 
--model pix2pix 
--direction AtoB
`

## other

`python "change latest model.py" checkpoints/pub/save/ "cyr_260_net_G.pth" checkpoints/pub/`
`python "change latest model.py" checkpoints/pub_ro/save/ "1300_net_G 1100 200 4 0004 cosine net256 continue 05_13 141.pth" checkpoints/pub_ro/`

create FID dataset
`python FID.py pub`
`python FID.py pub_ro`

calculate fid
`python -m pytorch_fid FID/fake FID/real`

get upload data
`python "get res.py"`

open visdom serve
`python -m visdom.server`

command picture

`python "datasets/combine_A_and_B ver2.py" --fold_A 34_Competition_1_Training_dataset/Training_dataset/img --fold_B ./34_Competition_1_Training_dataset/Training_dataset/label_img --fold_AB ./pub/`