import numpy as np
import pandas as pd

data = pd.read_csv('day2_input', sep=' ', header=None)
print(data)

commands = data.iloc[:,0].values
numbers = np.array(data.iloc[:,1].values, dtype='float')

hor = 0
vert = 0
counter = 0

for (c, n) in zip(commands, numbers):
    counter += 1
    if c == 'forward':
        hor += n
    elif c == 'down':
        # print("vert: ")
        # print(vert)
        # print("n: ")
        # print(n)
        vert += n
        # if np.isnan(vert):
        #     print(counter)
    elif c == 'up':
        print("vert: ")
        print(vert)
        print("n: ")
        print(n)
        vert -= n
        if np.isnan(vert):
            print(counter)

print(hor)
print(vert)