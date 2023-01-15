# Using the os builtin module in your working directory, create a directory named documents. Then in the documents directory, create 12 directories for each month named 01_sales, ..., 12_sales respectively. In response, print the sorted directory names in the documents directory.


import os
 
 
os.mkdir('documents')
 
dirnames = [f'{str(i).zfill(2)}_sales' for i in range(1, 13)]
for dirname in dirnames:
    path = os.path.join('documents', dirname)
    os.mkdir(path)
 
print(sorted(os.listdir('documents')))