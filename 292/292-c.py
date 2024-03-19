import sys
import math
from collections import defaultdict
input = sys.stdin.readline

N = int(input())

sum_dict = defaultdict(int)
sum_dict[1] = 1
for i in range(2,N):
    sum_dict[i] = 2

for i in range(2,N):
    for j in range(2,N//i):
        if i*j > N-1:
            break
        sum_dict[i*j] += 1

ans = 0
for i in range(1,N):
    ans += sum_dict[i] + sum_dict[N-i]

print(ans)