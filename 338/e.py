from atcoder.lazysegtree import LazySegTree

def op(x, y):
    return min(x, y)

def mapping(f, x):
    return f + x

def composition(f, g):
    return f + g

def main():
    N = ini()
    
    lsg = LazySegTree(op, 10**18, composition, mapping, 0, [0]*(2*N))
    for i in range(1, N+1):
        a, b = mapint0()
        a, b = (a, b) if a < b else (b, a)
        
        a_v = lsg.get(a)
        b_v = lsg.get(b)
        if a_v != b_v:
            print("Yes")
            return
        
        lsg.apply(a, b, i)
    print("No")

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