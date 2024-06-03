def f_dash(x, A, B):
    return (-1/2)*A*pow(x, -3/2) + B

def f(x, A, B):
    return A*pow(x, -1/2) + B*(x-1)

def main():
    A, B = mapint()
    
    l, r = 1, 2*A
    
    while r-l > 1:
        m = (l+r)//2
        if f_dash(m, A, B) < 0:
            l = m
        else:
            r = m
    
    l_v = f(l, A, B)
    r_v = f(r, A, B)
    print(min(l_v, r_v))

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