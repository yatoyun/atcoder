import sys
input = sys.stdin.readline

def main():
    N, W = map(int, input().split())
    
    dp = [[0] * (W+1) for _ in range(N+1)]
    
    for i in range(N):
        v, w = map(int, input().split())
        for j in range(W+1):
            dp[i][j] = max(dp[i][j], dp[i][j-1]) if j > 0 else dp[i][j]
            dp[i+1][j] = max(dp[i][j-w]+v, dp[i][j]) if j >= w else dp[i][j]

    
    print(dp[N][W])

if __name__ == "__main__":
    main()