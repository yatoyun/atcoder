import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
    order = list(map(int, input().split()))
    dicide = order[0]


    if dicide == 1:
        A[order[1]-1] = order[2]
    elif dicide == 2:
        print(A[order[1]-1])

