import cv2
import matplotlib.pyplot as plt
from tqdm import tqdm
for idx in tqdm(range(100000)):
    directory = "../dataset/Y/"
    imname = "train_mask_{}.png".format(idx)
    im = cv2.imread(directory + imname)
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(gray,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2:]
    annotation = str(imname)
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        annotation += " {},{},{},{},0".format(x, y, x+w, y+h)
    if len(contours) > 0:
        print(annotation)