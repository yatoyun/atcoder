def calc(v, k, bottom):
    return v/bottom - 1200/(k**(1/2))

def main():
    N = ini()
    P = lint()
    
    bottom = [0]
    for i in range(N):
        bottom.append(bottom[-1] + 0.9**i)
    
    dp = [[0]*(N+1) for _ in range(N+1)]
    
    for i in range(N):
        for j in range(i+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            curr = dp[i][j] + P[-(i+1)]*(0.9**(j))
            dp[i+1][j+1] = max(dp[i+1][j+1], curr)
        
    ans = -float("inf")
    for i in range(1,N+1):
        ans = max(ans, calc(dp[N][i], i, bottom[i]))
    print(ans)
            

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