def main():
    N = ini()
    S = lstr()
    C = lint()
    
    dp = [[[float("inf")]*2 for _ in range(2)] for _ in range(N+1)]
    dp[1][0][0] = C[0] if S[0] != "0" else 0
    dp[1][1][0] = C[0] if S[0] != "1" else 0
    for i in range(1,N):
        cost = C[i]
        for j in range(2):
            dp[i+1][j][0] = dp[i][(j+1)%2][0]
            dp[i+1][j][1] = min(dp[i][j][0], dp[i][(j+1)%2][1])
            if S[i] != str(j):
                dp[i+1][j][0] += cost
                dp[i+1][j][1] += cost
    errprint(dp[1:])
    print(min(dp[N][0][1], dp[N][1][1]))
    

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