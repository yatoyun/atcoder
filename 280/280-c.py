import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

S += "1"

for i, (s, t) in enumerate(zip(S, T)):
    if s != t:
        print(i+1)
        break