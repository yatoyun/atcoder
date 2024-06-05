def main():
    N, M = mapint()
    A = lint()
    
    sums = [0]
    for i in range(N):
        sums.append(sums[-1]+A[i])
    
    curr = 0
    for i in range(M):
        curr += A[i] * (i+1)

    ans = curr
    for i in range(0, N-M):
        curr = curr - (sums[M+i] - sums[i]) + M * A[M+i]
        ans = max(ans, curr)
    
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
