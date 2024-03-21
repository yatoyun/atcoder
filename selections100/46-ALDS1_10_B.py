import sys
input = sys.stdin.readline

def main():
    N = int(input())
    
    M = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
    
    for i in range(1, N):
        for start_i in range(N - i):
            end_i = start_i + i
            dp[start_i][end_i] = min([dp[start_i][k] + dp[k+1][end_i] + M[start_i][0]*M[k][1]*M[end_i][1] for k in range(start_i, end_i)])
        # for a in dp:
        #     print(a)
    print(dp[0][-1])
    
    

if __name__ == "__main__":
    main()