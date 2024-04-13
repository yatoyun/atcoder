from math import lcm

def calc_divide2(a):
    cnt = 0
    while a > 0:
        if a % 2 == 0:
            cnt += 1
            a //= 2
        else:
            break
    return cnt
def main():
    N, M = mapint()
    A = lint()
    
    lcm_v = A[0] // 2
    divide2 = calc_divide2(A[0]//2)
    for a in A[1:]:
        lcm_v = lcm(a // 2, lcm_v)
        curr_divide2 = calc_divide2(a//2)
        if divide2 != curr_divide2:
            print(0)
            return
    print(M//lcm_v - M//(2*lcm_v))

def ini(): return int(input())
def mapint(): return map(int, input().split())
def mapint0(): return map(lambda x: int(x)-1, input().split())
def mapstr(): return input().split()
def lint(): return list(map(int, input().split()))
def lint0(): return list(map(lambda x: int(x)-1, input().split()))
def lstr(): return list(input().rstrip())
def errprint(*x): return None if atcenv else print(*x, file=sys.stderr) 

if __name__=="__main__":
    import sys, os
    input = sys.stdin.readline
    atcenv = os.environ.get("ATCODER", 0)

    main()