def main():
    N = ini()
    A = []
    B = []
    
    A_sum = 0
    for i in range(N):
        a, b = mapint()
        A.append(a)
        B.append(b)
        A_sum += a
    
    ans = 0
    for i in range(N):
        a, b = A[i], B[i]
        lest_sum = A_sum - a
        ans = max(ans, lest_sum+b)
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