import cv2
import matplotlib.pyplot as plt
from tqdm import tqdm
import threading

num_processes = 40
tot_img = 100000
step = tot_img // num_processes
annotations = [""] * num_processes

def extract(start_idx, end_idx, i):
    for idx in tqdm(range(start_idx, end_idx)):
        directory = "../dataset/ynet/Y/"
        imname = "train_mask_{}.png".format(idx)
        im = cv2.imread(directory + imname)
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        contours, hierarchy = cv2.findContours(gray,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2:]
        annotation = str(imname)
        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            annotation += " {},{},{},{},0".format(x, y, x+w, y+h)
        if len(contours) > 0:
            annotations[i] += annotation + '\n'


if __name__ == '__main__':
    processes = []
    for i in range(num_processes):
        processes.append(threading.Thread(target=extract, args=(i*step, (i+1)*step, i,)))

    for p in processes:
        p.start()

    for p in processes:
        p.join()
        
    output = ""
    for i in range(num_processes):
        output += annotations[i]
    print(output)
