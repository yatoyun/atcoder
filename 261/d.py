from collections import defaultdict
def main():
    N, M = mapint()
    X = lint()
    
    bounus = defaultdict(int)
    for i in range(M):
        c, y = mapint()
        bounus[c] = y
    
    dp = [[-1]*(N+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(N):
            if dp[i][j] == -1:
                break
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + X[i]+bounus[j+1])
            dp[i+1][0] = max(dp[i+1][0], dp[i][j])
    print(max(dp[N]))

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