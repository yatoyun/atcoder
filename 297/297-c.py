import sys
input = sys.stdin.readline

H, W = map(int, input().split())

S = [input().rstrip() for _ in range(H)]


for i in range(H):
    for j in range(W-1):
        if S[i][j] == S[i][j+1] == "T":
            S[i] = S[i][:j] + "P" + S[i][j+1:]
            S[i] = S[i][:j+1] + "C" + S[i][j+2:]

for s_line in S:
    print(s_line)

