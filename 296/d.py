def bSearch(l, r, a):
    while r - l > 1:
        m = (l + r) // 2
        if m >= a:
            r = m
        else:
            l = m
    return r

def main():
    N, M = mapint()
    
    ans = float("inf")
    for a in range(1, int(M**0.5)+2):
        b = M // a + 1 if M % a else M // a
        if b > N:
            continue
        if a > b:
            break
        ans = min(ans, a*b)
    print(ans if ans != float("inf") else -1)

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