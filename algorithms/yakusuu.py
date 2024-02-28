import sys
input = sys.stdin.readline


x = int(input())

count = 0

for j in range(1,int(x**0.5)+1):
        if x%j==0:
            if j**2 == x:
                count += 1
            else:
                count += 2
print(count)