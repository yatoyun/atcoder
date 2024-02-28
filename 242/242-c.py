import sys
input = sys.stdin.readline

def main():
    MAX = 998244353

    N = int(input())
    dp = [[0]*11 for _ in range(N+1)]

    dp = [[0]*11 for _ in range(N+1)]
    for i in range(1,10):
        dp[1][i] = 1
    for i in range(2, N+1):
        for j in range(1, 10):
            dp[i][j] =  (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1])%MAX

    print(sum(dp[N])%MAX)

if __name__ == "__main__":
    main()