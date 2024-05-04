def main():
    N = ini()
    A = lint()
    
    A = [A[i]-i-1 for i in range(N)]
    
    A.sort()
    
    def get_median(x):
        if len(x)%2==1:
            return x[len(x)//2]
        else:
            return (x[len(x)//2-1]+x[len(x)//2])//2
    
    med = get_median(A)
    ans = 0
    for a in A:
        ans += abs(a-med)
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