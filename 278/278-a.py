import sys
input = sys.stdin.readline

n,k = map(int, input().split())
A = list(map(int, input().split()))

if n <= k:
    for i in range(n):
        print(0, end=" ")
    exit(0)

for a in A[k:]:
    print(a, end=" ")
for i in range(k):
    print(0, end=" ")
