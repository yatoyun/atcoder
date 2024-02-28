import sys
from collections import defaultdict
input = sys.stdin.readline

N= int(input())

A = list(map(int, input().split()))

M = int(input())

B = list(map(int, input().split()))


X = int(input())


dict = defaultdict(bool)
for i in range(X+1):
    dict[i] = False
for b in B:
    dict[b] = True


dp = [0 for i in range(X+1)]

dp[0] = 1
for i in range(X+1):
    if dp[i] == 0:
        continue
    for j in range(N):

        if not dict[i + A[j]]:
            if i + A[j] <= X:
                dp[i + A[j]] = 1

if dp[X] != 0:
    print("Yes")
else:
    print("No")



