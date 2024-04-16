def main():
    N, S = mapint()
    cards = [[0]*2 for _ in range(N)]
    
    for i in range(N):
        a, b = mapint()
        cards[i][0] = a
        cards[i][1] = b
    
    dp = [[False]*(S+1) for _ in range(N+1)]
    dpS = [[""]*(S+1) for _ in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S+1):
            if j - cards[i][0] >= 0:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-cards[i][0]]
                dpS[i+1][j] = dpS[i][j-cards[i][0]] + "H" if dp[i][j-cards[i][0]] and len(dpS[i+1][j]) <= i else dpS[i+1][j]
            if j - cards[i][1] >= 0:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-cards[i][1]]
                dpS[i+1][j] = dpS[i][j-cards[i][1]] + "T" if dp[i][j-cards[i][1]] and len(dpS[i+1][j]) <= i else dpS[i+1][j]
    print("Yes" if dp[N][S] else "No")
    if dp[N][S]:
        print(dpS[N][S])
    

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
