import pandas as pd

fp = open('/home/tailoc/Downloads/GIDS_dataset/CAN_IDS/CAN_ID_cut_first_zero.txt', 'r')

content = fp.readlines()
content = content[0].split(",")

file = open('/home/tailoc/Downloads/GIDS_dataset/CAN_IDS/one_CAN_ID_as_3_digits.txt','w')

for i in range(len(content)):
	for j in range(len(content[i])):
		if (content[i][j] != ','):
			file.write(content[i][j])

