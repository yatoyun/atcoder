import sys
input = sys.stdin.readline

def main():
    n, k = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]

    dp = [False for _ in range(n)]
    ep = [False for _ in range(n)]

    dp[0] = ep[0] = True
    for i in range(1,n):
        if dp[i-1]:
            if abs(A[i-1] - A[i]) <= k:
                dp[i] = True
            if abs(A[i-1] - B[i]) <= k:
                ep[i] = True
        
        if ep[i-1] == 1:
            if abs(B[i-1] - A[i]) <= k:
                dp[i] = True
            if abs(B[i-1] - B[i]) <= k:
                ep[i] = True
    if dp[-1] == 1 or ep[-1] == 1:
        print("Yes")
    else:
        print("No")
if __name__ == "__main__":
    main()