def main():
    N = ini()
    S = list(map(int,lstr()))
    
    dp = [[0]*2 for _ in range(N+1)]
    
    for i in range(N):
        dp[i][S[i]] = 1
    
    for i in range(N-1):
        for j in range(2):
            if j * S[i+1] == 1:
                dp[i+1][0] += dp[i][j]
            else:
                dp[i+1][1] += dp[i][j]
    
    ans = 0
    for i in range(N):
        ans += dp[i][1]
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
