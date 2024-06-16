def main():
    N, l, r = mapint()
    
    A = list(range(1, N+1))
    
    left = A[:l-1]
    mid = A[l-1:r]
    right = A[r:]
    mid = mid[::-1]
    ans = []
    ans.extend(left)
    ans.extend(mid)
    ans.extend(right)
    print(*ans, sep=" ")
    

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