import numpy as np
import pandas as pd

df = pd.read_csv('day6/day6_input', sep=',', header=None)
data = df.to_numpy()[0,:]
print(data)

store = np.zeros(9, dtype=int)
for x in data:
    store[x] += 1
print("Initial store: ", store)

for i in range(256):
    store[7] += store[0]
    store = np.roll(store, -1)
    print("Day ", i+1, store)

print(np.sum(store))