import numpy as np

data = np.fromfile('day7/day7_input', sep=',', dtype=int)
#print(data)


# PART 1:
m = round(np.median(data))
print("Median: ", m)

fuel = np.sum([np.abs(x-m) for x in data])
print("Fuel: ", fuel)
print()

# PART 2:
n = int(np.floor(np.mean(data)))
print("Mean: ", n)

best = m
test = 10000000000
for t in range(m, n+1):
    print("Best: ", best)
    fuel2 = np.sum([0.5*(np.abs(x-t)*(np.abs(x-t) + 1)) for x in data])
    if fuel2 < test:
        best = t
        test = fuel2

print("Best position: ", t)
print("New fuel: ", fuel2)
