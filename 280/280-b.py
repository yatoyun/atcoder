import sys
input = sys.stdin.readline

N = int(input())

S = list(map(int, input().split()))


current_sum = 0
for i in range(N):
    ans = S[i] - current_sum
    current_sum += ans

    print(ans, end=" ")

