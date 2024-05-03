def main():
    N = ini()
    
    xyz = [lint() for _ in range(N)]
    Z = sum([z for x, y, z in xyz])
    dp = [[float("inf")]*(Z+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        x, y, z = xyz[i]
        need_votes = (x+y)//2+1-x if y > x else 0
        for j in range(Z+1):
            if j < z:
                dp[i+1][j] = dp[i][j]
                continue
            dp[i+1][j] = min(dp[i][j], dp[i][j-z]+need_votes)
    # errprint(dp)
    ans = min(dp[N][Z//2+1:])
    print(ans)

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