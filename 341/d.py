from math import lcm

def calc(x, N, M):
    cnt_N_divided = x // N
    cnt_M_divided = x // M
    cnt_NM_divided = x // lcm(N, M)
    cnt = cnt_N_divided + cnt_M_divided - 2 * cnt_NM_divided
    return cnt

def main():
    N, M, K = mapint()
    N, M = sorted([N, M])
    
    l, r = 0, 10**25+1
    while r-l > 1:
        mid = (l+r)//2
        errprint(mid, calc(mid, N, M))
        if calc(mid, N, M) < K:
            l = mid
        else:
            r = mid
    print(r)

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