run extractBBS.py to generate train.txt
run dataset_splitter.py
run dataset_repairer.py
move train.txt, val.txt and test.txt from data to outer dir
change batch size in cfg.py
run `python train.py -l 0.001 -g 1 -pretrained ./yolov4.conv.137.pth -classes 1 -dir ../dataset/ynet/X`


image size set as 320. Search all for 320 to change size
