import sys
input = sys.stdin.readline

N, M = map(int, input().split())

S = []
for i in range(N):
    S.append(input().rstrip())

ans = 0
input_list=[]
for _ in range(M):
    T = input().rstrip()
    if T in input_list:
        continue
    input_list.append(T)
    for s in S:
        if s.endswith(T):
            ans += 1

print(ans)


