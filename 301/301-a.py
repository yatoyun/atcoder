import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()

win_min = N / 2

T_count = 0
A_count = 0

for s in S:
    if s == "T":
        T_count += 1
        if T_count >= win_min:
            print("T")
            exit()
    else:
        A_count += 1
        if A_count >= win_min:
            print("A")
            exit()
