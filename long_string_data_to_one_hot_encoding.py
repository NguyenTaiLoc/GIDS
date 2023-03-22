import pandas as pd
from IPython.display import display
import string
import matplotlib.pyplot as plt
import numpy as np

#loading CAN IDs from file
fp = open('/home/tailoc/Downloads/GIDS_dataset/CAN_IDS/test_data.txt', 'r')
content = fp.readlines()

data = []
for i in range(len(content[0])):
	if (content[0][i] != ','):
		data.append(content[0][i])

#one hot encoding data
one_hot_encoding = pd.get_dummies(data)


#checking for missing column in hexa and fill with zeros [0...9 a...f]
for character in string.ascii_lowercase[0:6] + string.digits[0:]:
    if character not in one_hot_encoding.columns:
    	one_hot_encoding[character] = 0

#plot data to image for checking
ax = plt.axes()
ax.set_facecolor('#000000')
plt.imshow(one_hot_encoding)
plt.show()