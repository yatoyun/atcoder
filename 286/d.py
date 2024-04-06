def main():
    N, X = mapint()
    
    dp = [[False] * (X+1) for _ in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        a, b = mapint()
        for j in range(b+1):
            v = a * (j)
            for k in range(X-v+1):
                dp[i+1][k+v] |= dp[i][k]
    print("Yes" if dp[N][X] else "No")

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