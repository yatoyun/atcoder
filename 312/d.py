def main():
    S = lstr()
    mod = 998244353
    
    dp = [[0]*(len(S)+1) for _ in range(len(S)+1)]
    
    dp[0][0] = 1
    for i in range(len(S)):
        if S[i] == "(":
            for j in range(len(S)):
                dp[i+1][j+1] = dp[i][j] % mod
        elif S[i] == ")":
            for j in range(1,len(S)+1):
                dp[i+1][j-1] = dp[i][j] % mod
        else:
            for j in range(len(S)):
                dp[i+1][j+1] = dp[i][j] % mod
            for j in range(1,len(S)+1):
                dp[i+1][j-1] += dp[i][j] % mod
    
    print(dp[len(S)][0]%mod)
        
    
    
    
    

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