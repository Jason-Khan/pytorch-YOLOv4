file1 = open('data/train.txt', 'r') 
lines = file1.readlines()
file1.close()

lines = [l[:5] + l[10:] for l in lines]

file1 = open('data/train.txt', 'w') 
file1.writelines(lines) 
file1.close() 

file1 = open('data/val.txt', 'r') 
lines = file1.readlines()
file1.close()

lines = [l[:5] + l[10:] for l in lines]

file1 = open('data/val.txt', 'w') 
file1.writelines(lines) 
file1.close() 

file1 = open('data/test.txt', 'r') 
lines = file1.readlines()
file1.close()

lines = [l[:5] + l[10:] for l in lines]

file1 = open('data/test.txt', 'w') 
file1.writelines(lines) 
file1.close() 