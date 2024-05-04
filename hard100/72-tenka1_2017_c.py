def main():
    N = ini()
    
    for h in range(1, 3501):
        for n in range(1, 3501):
            if (4*h*n-N*(n+h) == 0):
                continue
            if (N*h*n) % (4*h*n-N*(n+h)) == 0:
                w = (N*h*n) // (4*h*n-N*(n+h))
                if w < 0:
                    continue
                print(h, n, w)
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