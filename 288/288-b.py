import sys
input = sys.stdin.readline

N, K = map(int, input().split())

name_list = []

for i in range(N):
    if i >= K:
        break
    name_list.append(input().rstrip())

name_list.sort()

for name in name_list:
    print(name)


