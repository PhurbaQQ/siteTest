import re

with open('D:\\fileOne.txt', 'r') as f:
    file = f.read()
    

file = re.sub(r'\s' , '_', file,1)
file = re.sub(r'\s' , '-', file,1)
file = re.sub(r'\s' , '/', file,1)
file = re.sub(r'\s' , '_', file,1)
file = re.sub(r'\s' , '-', file,1)
file = re.sub(r'\s' , '/', file,1)
file = re.sub(r'\s' , '_', file,1)

with open('D:\\fileTwo.txt', 'w') as f:
    f.writelines(file)
    