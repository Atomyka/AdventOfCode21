import numpy as np

data = np.loadtxt('day1/day1_test')
#print(data)

#### PART 1 ###
'''Part 1'''
def measure(input):
    diff = np.diff(input)
    log = [1 for x in diff if x > 0] 
    print(log)   
    return np.sum(log)           


### PART 2 ###
data_roll = data + np.roll(data, 1)  + np.roll(data, 2) 
data_roll = data_roll[2:]
print(measure(data_roll))

