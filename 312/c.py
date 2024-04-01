from bisect import bisect_left, bisect_right

def main():
    N, M = mapint()
    
    A = lint()
    B = lint()
    
    A.sort()
    B.sort()

    l = -1
    r = 10**9+1000
    while r-l > 1:
        m = (l+r)//2
        sell_num = bisect_right(A, m)
        buy_num = M - bisect_left(B, m)
        if sell_num < buy_num:
            l = m
        else:
            r = m
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