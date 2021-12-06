import numpy as np
import pandas as pd

#data = np.fromfile('day3/day3_input', dtype=int, sep=' ')
#data = np.loadtxt('day3/day3_test', dtype=bytes)
data = np.loadtxt('day3/day3_test', dtype=int)

columns = np.zeros(5)

for x in data:
    for p in range(1, 6):        
        if np.remainder(x, np.power(10,p)) != 0:
            columns[-p] += 1
            x -= np.power(10,p-1)

print("Number of bits per column: ", columns)

gamma = 0
epsilon = 0
N = len(data)
print("N: ", N)

for p in range(0,5):
    if columns[4-p] > N/2:
        print(columns[4-p])
        gamma += np.power(2, p)
    else:
        print(columns[4-p])
        epsilon += np.power(2, p)

print("Gamma: ", gamma)
print("Epsilon: ", epsilon)
print("Power: ", gamma*epsilon)

