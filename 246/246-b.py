import math

x, y = [int(x) for x in input().split()]

z = math.sqrt(x ** 2 + y ** 2)

x1 = x * 1 / z
y2 = y * 1 / z

print(x1, y2)