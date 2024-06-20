from bisect import bisect_left, bisect_right
def main():
    N, K = mapint()
    A = lint()
    sortedA = sorted(A)
    
    visited = set()
    for i, a in enumerate(A):
        left = bisect_left(sortedA, a)
        right = bisect_right(sortedA, a)
        
        for index in range(left, right):
            if index in visited:
                continue
            if abs(i-index) % K == 0:
                visited.add(index)
                break
            
        else:
            print("No")
            return
    print("Yes")
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