from atcoder.lazysegtree import LazySegTree

def op(x, y):
    if x[0] > y[0]:
        return x
    return y

def mapping(f, x):
    return (f+x[0], x[1])

def composition(f, g):
    return f + g

def main():
    N, M = mapint()
    X = lint0()
    lazyT = LazySegTree(op, (-1, -1), mapping, composition, 0, [(0, i) for i in range(N)])
    for i in range(1,M):
        x, y = X[i-1], X[i]
        if x < y:
            x, y = y, x
        diff = x-y
        lazyT.apply(y, x, diff)
        diff = N-x+y
        lazyT.apply(0, y, diff)
        lazyT.apply(x, N, diff)
        # print("i:", i, "x:", x, "y:", y)
        # for i in range(N):
        #     print(lazyT.get(i), end=" ")
        # print()
    score, index = lazyT.all_prod()
    
    ans = 0
    for i in range(1,M):
        x, y = X[i-1], X[i]
        if x < y:
            x, y = y, x
        
        if x > index >= y:
            ans += N-x+y
        else:
            ans += x-y
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