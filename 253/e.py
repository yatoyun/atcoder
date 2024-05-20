def main():
    mod = 998244353
    n, m, k = mapint()
    
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, m+1):
        dp[1][i] = 1 + dp[1][i-1]
    for i in range(1,n):
        for j in range(1, m+1):
            unessential = 0
            if k != 0:
                unessential = dp[i][j+k-1] if j+k-1 <= m else dp[i][-1]
                unessential -= dp[i][j-k] if j-k > 0 else dp[i][0]
            dp[i+1][j] = dp[i][-1] - unessential
            if dp[i+1][j] < 0:
                dp[i+1][j] += mod
            dp[i+1][j] += dp[i+1][j-1]
            dp[i+1][j] %= mod
    print((dp[-1][-1])%mod)

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
