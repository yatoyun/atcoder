def main():
    N = ini()
    A = [lstr() for _ in range(N)]
    B = [lstr() for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if A[i][j] != B[i][j]:
                print(i+1, j+1)
                return

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