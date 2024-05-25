from sortedcontainers import SortedList

def main():
    N = ini()
    
    rights = SortedList()
    ranges = []
    for i in range(N):
        l, r = mapint()
        ranges.append((l, r))
    
    ans = 0
    ranges.sort(key=lambda x: x[0])
    for i in range(N):
        l, r = ranges[i]
        index = rights.bisect_left(l)
        num = len(rights) - index
        ans += num
        rights.add(r)
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