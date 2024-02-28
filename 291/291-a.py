import sys
input = sys.stdin.readline

S = input().rstrip()

for i, s in enumerate(S):
    if s.isupper():
        print(i+1)