import pandas as pd
from IPython.display import display

final_data = []

#open and read data from file txt
fp = open('/home/tailoc/Downloads/GIDS_dataset/data/RPM_dataset.csv', 'r')
content = fp.readlines()


#split each line data by comma, get CAN ID then cut first zero
for i in range(len(content)):
    result = [x.strip() for x in content[i].split(',')]
    final_data.append(result[1][1:])

#write data to file
fw = open('/home/tailoc/Downloads/GIDS_dataset/CAN_IDS/RPM_dataset.txt', 'w')
fw.write(str(final_data))
