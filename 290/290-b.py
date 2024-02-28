import sys
input = sys.stdin.readline

N, K = map(int, input().split())

S = input().rstrip()

ans = ""
total_num = 0

for i, s in enumerate(S):
    if total_num >= K:
        ans += "x"
        continue

    if s == "o":
        ans += "o"
        total_num += 1
    elif s == "x":
        ans += "x"

print(ans)