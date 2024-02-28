import numpy as np

a = []
coodinate = []

for _ in range(3):
	a.append([int(x) for x in input().split()])
b = np.array(a).T

for i in range(2):
    u, counts = np.unique(b[i], return_counts=True)
    coodinate.extend(u[counts == 1])

print(coodinate[0], coodinate[1])