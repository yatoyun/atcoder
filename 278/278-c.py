import sys
from collections import defaultdict
input = sys.stdin.readline

dict = defaultdict(set)

n, q = map(int, input().split())

for i in range(q):
    t, a, b = map(int, input().split())

    if t == 1:
        dict[a].add(b)
    if t == 2:
        if b in dict[a]:
            dict[a].remove(b)
    if t == 3:
        if a in dict[b] and b in dict[a]:
            print("Yes")
        else:
            print("No")
