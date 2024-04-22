from collections import defaultdict
from atcoder.lazysegtree import LazySegTree
from atcoder.segtree import SegTree
def op(x, y):
    return max(x, y)

def mapping(lazy_upper, data_lower):
    return max(data_lower, lazy_upper)

def composition(lazy_upper, lazy_lower):
    return max(lazy_upper, lazy_lower)

##### seg tree
def main():
    N, D = mapint()
    A = lint()
    
    max_A = max(A)
    segTree = SegTree(op, 0, [0]*(max_A+1))
    ans = 0
    for i in range(N):
        curr = A[i]
        left = max(0, curr-D)
        right = min(max_A+1, curr+D+1)
        l = segTree.prod(left, right)
        segTree.set(curr, l+1)
    print(segTree.all_prod())
    
##### lazy seg tree
# def main():
#     N, D = mapint()
#     A = lint()
    
#     max_A = max(A)
#     lazyTree = LazySegTree(op, 0, mapping, composition, 0, [0]*(max_A+1))
#     ans = 0
#     for i in range(N):
#         curr = A[i]
#         l = lazyTree.get(curr)
#         left = max(0, curr-D)
#         right = min(max_A+1, curr+D+1)
#         lazyTree.apply(left, right, l+1)
#         ans = max(ans, l+1)
#         errprint(left, right, l+1)
#     print(ans)

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