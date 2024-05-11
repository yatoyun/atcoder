def main():
    N = ini()
    A = lint()
    
    mod = 998244353
    diff = [0]*N
    for i in range(1,N):
        diff[i] = 10**(len(str(A[i])))
    
    sums = [0]*N
    sums[0] = diff[0]
    for i in range(1, N):
        sums[i] = sums[i-1]+diff[i]
    
    sums2 = [0]*N
    sums2[0] = A[0]
    for i in range(1, N):
        sums2[i] = sums2[i-1]+A[i]
    
    ans = 0
    for i in range(N-1):
        ans += (A[i]*(sums[-1]-sums[i])+(sums2[-1]-sums2[i])) % mod
    print(ans%mod)
    

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