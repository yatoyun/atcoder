import sys
import math
input = sys.stdin.readline

import random

def is_prime3(q,k=50):
    q = abs(q)
    #計算するまでもなく判定できるものははじく
    if q == 2: return True
    if q < 2 or q&1 == 0: return False

    #n-1=2^s*dとし（但しaは整数、dは奇数)、dを求める
    d = (q-1)>>1
    while d&1 == 0:
        d >>= 1

    #判定をk回繰り返す
    for i in range(k):
        a = random.randint(1,q-1)
        t = d
        y = pow(a,t,q)
        #[0,s-1]の範囲すべてをチェック
        while t != q-1 and y != 1 and y != q-1:
            y = pow(y,2,q)
            t <<= 1
        if y != q-1 and t&1 == 0:
            return False
    return True

K = int(input())
current_left = K

if is_prime3(K):
    print(K)
    exit()

i = 2
while i <= 2*10**6:
    current_left = current_left // math.gcd(current_left, i)
    if current_left == 1:
        print(i)
        exit()

    i += 1

print(current_left)

