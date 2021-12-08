import numpy as np
import pandas as pd

#data = np.fromfile('day5/day5_test', sep=',')
df = pd.read_csv('day5/day5_test', sep=',', header=None, engine='python')
x1 = df[0].to_numpy()
y1 = df[1].to_numpy()
y2 = df[2].to_numpy()
print(y1)

interim = np.zeros(2*len(x1))
for y in y1:
    for c in y:
        print(c)
        print(type(c))