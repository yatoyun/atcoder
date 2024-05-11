from bisect import bisect_left, bisect_right

def main():
    N = ini()
    A = lint()
    A.sort()
    
    sums = [A[0]]
    mod = 10**8
    for i in range(1, N):
        sums.append(sums[-1]+A[i])
    
    ans = 0
    for i in range(N-1):
        over_index = bisect_left(A, mod-A[i], i+1)
        ans += (A[i]*(N-i-1) + (sums[-1]-sums[i])-(N-over_index)*mod)
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