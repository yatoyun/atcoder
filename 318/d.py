def main():
    N = ini()
    D = [lint() for _ in range(N)]
    
    dp = [0]*(1<<N)
    
    for b in range((1<<N)-1):
        l = -1
        for i in range(N):
            if (b>>i)&1:
                continue
            l = i
            break
        
        for i in range(N):
            if (b>>i)&1:
                continue
            nb = b | (1<<i) | (1<<l)
            if i <= l:
                dp[nb] = max(dp[nb], dp[b])
                continue
            dp[nb] = max(dp[nb], dp[b] + D[l][i-l-1])
    errprint(dp)
    print(dp[-1])
        
            

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