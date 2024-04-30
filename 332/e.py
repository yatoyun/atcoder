from collections import defaultdict

def main():
    N, K, P = mapint()
    
    plans = []
    for i in range(N):
        A = lint()
        plans.append(A)
    
    dp = [defaultdict(lambda: float("inf")) for _ in range(N+1)]
    
    dp[0][tuple([0]*5)] = 0
    for i in range(N):
        dic = dp[i]
        for k, v in dic.items():
            if v == float("inf"):
                continue
            dp[i+1][k] = v
        for k, v in dic.items():
            new_arr = []
            for j in range(K):
                if k[j]+plans[i][j+1] < P:
                    new_arr.append(k[j]+plans[i][j+1])
                else:
                    new_arr.append(P)
            new_arr = tuple(new_arr)
            dp[i+1][new_arr] = min(dp[i+1][new_arr], v+plans[i][0])
    
    print(dp[N][tuple([P]*K)] if dp[N][tuple([P]*K)] != float("inf") else -1)
    
    

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