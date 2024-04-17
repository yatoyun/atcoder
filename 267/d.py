def main():
    N, M =  mapint()
    A = lint()
    
    dp = [[-float("inf")]*N for _ in range(M+1)]
    for i in range(N):
        dp[1][i] = max(A[i], dp[1][i-1] if i>0 else -float("inf"))
    for i in range(1,M):
        for j in range(i, N):
            dp[i+1][j] = max(dp[i+1][j-1], dp[i][j-1]+(i+1)*A[j])
    errprint(dp)
    print(dp[M][N-1])

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
