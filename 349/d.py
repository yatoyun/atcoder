from math import log2
import sys
sys.setrecursionlimit(10**7)

def solve(l, r, n):
    if l+1 == r:
        return [(l, r)]
    if l >= r:
        return []
    if n == 0:
        return [(l, l+1), (l+1, r)]
    
    left = (l // 2**n) * 2**n
    if l % (2**n) != 0:
        left += 2**n
    right = left + 2**n
    if right > r:
        return solve(l,r,n-1)
    
    left_side = solve(l, left, n)
    right_side = solve(right, r, n)
    return [*left_side, (left, right), *right_side]

def main():
    l, r = mapint()
    
    n = 60
    ans = solve(l, r, n)
    print(len(ans))
    for a in ans:
        print(*a)
    

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