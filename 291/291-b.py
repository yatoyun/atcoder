import sys
input = sys.stdin.readline

N = int(input())

X = list(map(int, input().split()))

X.sort()

ans = X[N:-N]


print(sum(ans)/(3*N))