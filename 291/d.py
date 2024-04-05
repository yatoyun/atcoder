def main():
    mod = 998244353
    
    N = ini()
    A = []
    B = []
    for _ in range(N):
        a, b = mapint()
        A.append(a)
        B.append(b)
    
    dp = [[0]*2 for _ in range(N+1)]
    dp[1][0] = 1
    dp[1][1] = 1
    for i in range(1,N):
        if A[i] != A[i-1]:
            dp[i+1][0] = dp[i][0]
        if B[i] != B[i-1]:
            dp[i+1][1] = dp[i][1]
        if A[i-1] != B[i]:
            dp[i+1][1] += dp[i][0]
        if B[i-1] != A[i]:
            dp[i+1][0] += dp[i][1]
        dp[i+1][0] %= mod
        dp[i+1][1] %= mod
    errprint(dp)
    print((dp[N][0]+dp[N][1])%mod)

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
