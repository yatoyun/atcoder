from math import log
def main():
    N = ini()
    
    dp = [0]*(N+1)
    for i in range(1, N+1):
        dp[i] = dp[i-1]+1
        j = 6
        while j <= i:
            dp[i] = min(dp[i], dp[i-j]+1)
            j *= 6
        j = 9
        while j <= i:
            dp[i] = min(dp[i], dp[i-j]+1)
            j *= 9
    print(dp[N])

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