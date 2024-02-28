import sys
input = sys.stdin.readline

def main():
    mod = 998244353

    N, M, K = map(int, input().split())

    dp = [[0]*(K+1) for _ in range(N+1)]

    dp[0][0] = 1

    for i in range(N):
        for j in range(K):
            for k in range(1, M+1):
                if j + k > K:
                    break
                dp[i+1][j+k] += dp[i][j]
    sum = 0
    for x in dp[-1]:
        sum += x
        sum %= mod
    print(sum)
                

    
if __name__ == "__main__":
    main()