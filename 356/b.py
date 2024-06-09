def main():
    N, M = mapint()
    A = lint()
    X = [0]*M
    for i in range(N):
        x = lint()
        for j in range(M):
            X[j] += x[j]
    
    check = True
    for j in range(M):
        if A[j] > X[j]:
            check = False
    
    print("Yes" if check else "No")
    
    

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