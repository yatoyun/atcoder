from collections import defaultdict
def main():
    MOD = 998244353
    n,m,k,s,t,x = mapint()
    s, t, x = s - 1, t - 1, x - 1
    
    edges = defaultdict(list)
    
    for _ in range(m):
        u,v = mapint0()
        edges[u].append(v)
        edges[v].append(u)
    
    dp = [[[0]*2 for _ in range(n)] for _ in range(k+1)]

    if s not in edges or t not in edges:
        print(0)
        return

    dp[0][s][0] = 1
    for i in range(k):
        for j in range(n):
            for b in range(2):
                if dp[i][j][b] == 0:
                    continue
                for v in edges[j]:
                    if v == x:
                        dp[i+1][v][(b+1)%2] += dp[i][j][b]
                        dp[i+1][v][(b+1)%2] %= MOD
                        continue
                    dp[i+1][v][b] += dp[i][j][b]
                    dp[i+1][v][b] %= MOD
    print(dp[k][t][0])
    
    
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
