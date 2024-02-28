import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()

checkpoint = set()
checkpoint.add((0,0))
x = 0
y = 0

for s in S:
    if s == "L":
        x -= 1
    elif s == "R":
        x += 1
    elif s == "U":
        y += 1
    elif s == "D":
        y -= 1


    if (x, y) in checkpoint:
        print("Yes")
        exit()
    else:
        checkpoint.add((x, y))


print("No")