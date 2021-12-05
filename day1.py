import numpy as np

data = np.loadtxt('day1_test')
#print(data)

#### PART 1 ###
'''Part 1'''
def measure(input):
    diff = np.diff(input)
    # log = [1 for x in diff if x > 0] 
    # print(log)   
    # return np.sum(log)       \
    counter = 0
    counter +=1 for x in diff if x > 0
    return counter        


# counter = 0
# for x in diff:
#     if x > 0:
#         counter += 1
# print(counter)


### PART 2 ###
# data0 = data[0:-2]
# data0 = np.append(data, [0,0])
# print(data0)
# data1 = data[1:-1]
# data1 = np.insert(data, 0, [0])
# data1 = np.append(data1, [0])
# data2 = data[2:]
# data2 = np.insert(data, 0, [0,0])

# data_roll = (data0 + data1 + data2)
# print(data_roll)

# data_roll = np.zeros(len(data)-2)
# for i in range(len(data_roll)):
#     data_roll[i] = data[i] + data[i+1] + data[i+2]
# print(data_roll)
# print(measure(data_roll))

data_roll = data + np.roll(data, 1)  + np.roll(data, 2) 
data_roll = data_roll[2:]
print(data_roll)
print(measure(data_roll))

