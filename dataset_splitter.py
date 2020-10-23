file1 = open('train.txt', 'r') 
lines = file1.readlines()

train = len(lines) // 10 * 8
val = len(lines) // 10 * 1

train_anno = lines[:train]
val_anno = lines[train:train+val]
test_anno = lines[train+val:]

file1 = open('data/train.txt', 'w') 
file1.writelines(train_anno) 
file1.close() 

file1 = open('data/val.txt', 'w') 
file1.writelines(val_anno) 
file1.close() 

file1 = open('data/test.txt', 'w') 
file1.writelines(val_anno) 
file1.close() 