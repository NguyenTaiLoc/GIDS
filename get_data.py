import pandas as pd
from IPython.display import display

        
# fp = open('/home/tailoc/Downloads/GIDS_dataset/data/normal_data.txt', 'w')

# with open('/home/tailoc/Downloads/GIDS_dataset/data/normal_run_data.txt','r') as file:
    # for line in file:
    #     st1 = line.split(" ")
    #     # print(type(st1[10]))
    #     if (len(st1[10]) == 4):
    #         fp.write(st1[10])
    #         fp.write(',')

fp = open('/home/tailoc/Downloads/GIDS_dataset/data/normal_data.txt', 'r')
   
content = fp.readlines()
content = content[0].split(",")
for i in range(len(content)):
    if content[i][0] != '0':
        print("FALSE")
    else:
        print("YES")