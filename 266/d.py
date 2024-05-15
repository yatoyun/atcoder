from collections import defaultdict
def main():
    N = ini()
    
    times = []
    XA = defaultdict(lambda: (0, 0))
    
    
    for i in range(N):
        t, x, a = mapint()
        times.append(t)
        XA[t] = (x, a)
    dp = [[-float("inf")]*5 for _ in range(times[-1]+1)]
    dp[0][0] = 0
    for i in range(times[-1]):
        for x in range(5):
            for d in [-1, 0, 1]:
                if 0 <= x+d < 5:
                    dp[i+1][x+d] = max(dp[i+1][x+d], dp[i][x])
        dp[i+1][XA[i+1][0]] = dp[i+1][XA[i+1][0]]+XA[i+1][1]
    print(max(dp[times[-1]]))

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