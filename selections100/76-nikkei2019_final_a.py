def main():
    N = ini()
    A = lint()
    
    sums = [0]*(N+1)
    for i in range(N):
        sums[i+1] = sums[i] + A[i]
    
    for k in range(1,N+1):
        maxv = 0
        for i in range(k,N+1):
            maxv = max(maxv, sums[i]-sums[i-k])
        print(maxv)
    

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