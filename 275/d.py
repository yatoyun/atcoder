from functools import lru_cache
import sys
sys.setrecursionlimit(10**7)

@lru_cache(None)
def solve(N):
    if N == 0:
        return 1
    return solve(N//2) + solve(N//3)

def main():
    N = ini()
    
    print(solve(N))

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