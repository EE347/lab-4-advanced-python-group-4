import numpy as np

x = np.ones((8, 8))
print('Before:')
print(x)

# Your code goes here
for i in range(1, x.shape[0]-1):
    for j in range(1, x.shape[1]-1):
        x[i][j] = 0

print('After:') 
print(x)