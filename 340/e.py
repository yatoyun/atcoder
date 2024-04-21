from atcoder.lazysegtree import LazySegTree

def op(x, y):
    return x+y

def mapping(lazy_upper, data_lower):
    return data_lower + lazy_upper

def composition(lazy_upper, lazy_lower):
    return lazy_upper + lazy_lower

def main():
    N, M = mapint()
    A = lint()
    B = lint()
    
    lazy_tree = LazySegTree(op, 2**31-1, mapping, composition, 0, A)
    
    for i in range(M):
        b = B[i]
        nums = lazy_tree.get(b)
        lazy_tree.set(b, 0)
        all_add = nums//N
        remain = nums%N
        lazy_tree.apply(0, N, all_add)
        errprint(b, nums, all_add, remain)
        if b + remain < N:
            lazy_tree.apply(b+1, b+remain+1, 1)
        else:
            lazy_tree.apply(b+1, N, 1)
            remain -= N - b - 1
            lazy_tree.apply(0, remain, 1)
            errprint((b+1, N), (0, remain))
    for i in range(N):
        print(lazy_tree.get(i), end=" ")

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