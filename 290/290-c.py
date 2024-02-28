import sys
input = sys.stdin.readline

N, K = map(int, input().split())

A = set(map(int, input().split()))

ans = 0

if len(A) <= K:
    K = len(A)

for i in range(K):
    if i in A:
        ans += 1
    else:
        break

print(ans)