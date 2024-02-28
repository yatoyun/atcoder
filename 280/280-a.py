import sys
input = sys.stdin.readline

H, W = map(int, input().split())

ans = 0

for i in range(H):
    ans += input().rstrip().count("#")

print(ans)