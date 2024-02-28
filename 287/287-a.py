import sys
input = sys.stdin.readline

N = int(input())

For_num = 0
Agin_num = 0

for i in range(N):
    S = input().rstrip()

    if S == "For":
        For_num += 1
    elif S == "Against":
        Agin_num += 1

if For_num > Agin_num:
    print("Yes")
else:
    print("No")