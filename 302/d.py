def main():
    N, M, D = mapint()
    A = sorted(lint(), reverse=True)
    B = sorted(lint(), reverse=True)
    
    ia = 0
    ib = 0
    while ia<N and ib<M:
        diff = abs(A[ia]-B[ib])
        if diff<=D:
            print(A[ia] + B[ib])
            return
        
        if A[ia]>B[ib]:
            ia += 1
        else:
            ib += 1
    print(-1)
            

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