def main():
    S = lstr()
    T = lstr()
    
    ans = []
    iS = 0
    iT = 0
    while iS < len(S) or iT < len(T):
        if S[iS] == T[iT]:
            ans.append(iT+1)
            iS += 1
            iT += 1
        else:
            iT += 1
    print(*ans)
    
    

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