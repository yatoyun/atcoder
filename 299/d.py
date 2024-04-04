def main():
    N = ini()
    S = [-1]*N
    S[0] = 0
    S[-1] = 1
    
    l, r = 0, N-1
    while r-l > 1:
        m = (l+r)//2
        print("? {}".format(m+1))
        sys.stdout.flush()
        ans = ini()
        
        if ans==0:
            S[m] = 0
            l = m
        else:
            S[l] = 1
            r = m
    print("! {}".format(l+1))

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