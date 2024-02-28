import sys
from math import gcd

input = sys.stdin.readline

# def solve():
#     N, D, K = map(int, input().split())

#     mas = set()

#     mas.add(0)
#     last_mas = 0
#     ans = [0 for _ in range(N)]
#     num = 0
#     while mas != set(range(N)):
#         x = (last_mas+D) % N
#         while True:
#             if x in mas:
#                 print("yes", x, num)
#                 x = (x+1) % N
#             else:
#                 break
#         mas.add(x)
#         num += 1
#         ans[x] = num
#         last_mas = x

#     for i in range(N):
#         print(i, ":" ,ans[i])

def lcm(x, y):
    return (x * y) // gcd(x, y)

def solve():
    N, D, K = map(int, input().split())
    if gcd(N, D) == 1:
        K -= 1
        if K == 0:
            print(0)

        else:
            print(D*K % N)
    else:
        reset_point = lcm(N, D)
        reset_timing = reset_point // D
        K -= 1
        if K == 0:
            print(0)

        else:
            print((D*(K % reset_timing) + K // reset_timing) % N)


T=int(input())
for _ in range(T):
    solve()
