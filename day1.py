import numpy as np

data = np.loadtxt('day1_input')

diff = np.diff(data)
print(len(diff))

log = [1 for x in diff if x > 0]
print(np.sum(log))

