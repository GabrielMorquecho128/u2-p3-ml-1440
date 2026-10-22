import numpy as np
# marco morquecho NC 1440
n = np.array([10, 20, 30, 40, 50])

print(n)
print(n[0])
print(n[3])
print(n[-1])
print(n[-2])

print("------------------------------")

n = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(n)
print(n[0, 0])
print(n[1, 2])
print(n[-1, -1])
print(n[-2, -2])
print("------------------------------")
# 3D array 2x(2x3)
n = np.array([
# 0
[
    [10, 20, 30],
    [40, 50, 60]
],
# 1
[

    [10, 20, 30],
    [100, 110, 120]
 ]
])
print(n)
print([0,0,0])
print("marco morquecho NC 1440")