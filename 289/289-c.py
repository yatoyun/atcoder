import sys
input = sys.stdin.readline
from itertools import combinations

def calc(orign_N, N, origin_M, A_list):
    ans = 0
    set_M = set(range(1, orign_N+1))
    for comb_N in combinations(range(origin_M), N):
        sum = set()
        for i in comb_N:
            sum = sum.union(A_list[i])
        if sum == set_M:
            ans += 1
    return ans

N, M = map(int, input().split())
A_list = []
ans = 0
for i in range(M):
    c = int(input())
    A_list.append(set(map(int, input().split())))

for i in range(1, M+1):
    ans += calc(N, i, M, A_list)

print(ans)