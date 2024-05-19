from collections import defaultdict

def main():
    N = ini()
    
    A = []
    B = []
    for _ in range(N):
        a, b = mapint()
        A.append(a)
        B.append(b)
    
    dp = [-1]*(1<<N)
    dp[0] = 0
    for i in range(1, 1<<N):
        flag = False
        for j in range(N-1):
            for k in range(j+1, N):
                if (i>>j)&1 and (i>>k)&1:
                    if A[j] != A[k] and B[j] != B[k]:
                        continue
                    if dp[i^(1<<j)^(1<<k)] == 0:
                        flag = True
                        break
        dp[i] = int(flag)
    
    print("Takahashi" if dp[-1] else "Aoki")

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