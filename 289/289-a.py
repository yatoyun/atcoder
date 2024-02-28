import sys
input = sys.stdin.readline

S = input().strip()

for s in S:
    if s == '1':
        print(0, end='')
    elif s == '0':
        print(1, end='')