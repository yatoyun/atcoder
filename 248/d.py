from collections import defaultdict
from bisect import bisect_left, bisect_right
def main():
    N = ini()
    A = lint()
    Q = ini()
    
    nums_indexes = defaultdict(list)
    for i in range(N):
        nums_indexes[A[i]].append(i+1)
    
    for _ in range(Q):
        l, r, x = mapint()
        indexes = nums_indexes[x]
        left = bisect_left(indexes, l)
        right = bisect_right(indexes, r)-1
        if left > right:
            print(0)
            continue
        print(right-left+1)
        
        

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