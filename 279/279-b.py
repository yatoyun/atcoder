import sys
from itertools import combinations
input = sys.stdin.readline

S = input()
T = input()

for a, b in combinations(range(len(S)),2):
    if S[a:b] == T.strip():
        print("Yes")
        exit()
print("No")
