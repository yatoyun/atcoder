import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

num_list = [0]*N

for i in range(Q):
    order, x = map(int, input().split())

    if order == 1:
        num_list[x-1] += 1
    elif order == 2:
        num_list[x-1] += 2

    else:
        if num_list[x-1] >= 2:
            print("Yes")
        else:
            print("No")
