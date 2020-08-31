import numpy as np
import math

b = input("Put an array range (number dividable to 3), press ENTER: ")
b = int(b)
myArray = np.zeros((b, b), dtype=int)
a = np.arange(1, 10)
np.random.shuffle(a)
s = 0
for l in range(int(b/3)):
    for i in range(b):
        for j in range(l*3, int(l*3+3)):
            myArray[i][j] = a[s]
            s = s + 1
        if i != 0:
            if math.fmod(i+1, 3) == 0:
                s = 0
                a = np.arange(1, 10)
                np.random.shuffle(a)
print(myArray)