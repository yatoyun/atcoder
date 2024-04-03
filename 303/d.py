def main():
    X, Y, Z = mapint()
    S = lstr()
    
    dp = [[float("inf")]*2 for _ in range(len(S)+1)]
    
    dp[0][0] = 0
    dp[0][1] = Z
    for i in range(len(S)):
        is_capitalize = S[i].isupper()
        if is_capitalize:
            dp[i+1][0] = min(dp[i][0]+Y, dp[i][1]+Z+Y)
            dp[i+1][1] = min(dp[i][1]+X, dp[i][0]+Z+X)
        else:
            dp[i+1][0] = min(dp[i][0]+X, dp[i][1]+Z+X)
            dp[i+1][1] = min(dp[i][1]+Y, dp[i][0]+Z+Y)
    errprint(dp)
    print(min(dp[-1]))

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