import sys
import numpy as np
input = sys.stdin.readline

n = int(input())

A = []

for i in range(n):
    B = list(map(int, input().split()))
    A.append(B)
S = input()
for i in range(len(A)):
    if S[i] == "L":
        A[i][0] *= -1
A = sorted(A, key=lambda x: (x[0], x[1]))
A = np.array(A)
i = 0
while i < len(A):
    n = np.count_nonzero(A[i] == A[i][1], axis=0)
    if A[i][0] + A[i+n-1][0] < 0:
        print("Yes")
        exit()
    i += n - 1
print("No")
