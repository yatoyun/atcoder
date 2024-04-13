from collections import defaultdict
from bisect import bisect_right

def main():
    H, W, r, s = mapint()
    curr = [r, s]
    
    wallsbyrow = defaultdict(list)
    wallsbycol = defaultdict(list)

    N = ini()
    for _ in range(N):
        r, c = mapint()
        wallsbyrow[r].append(c)
        wallsbycol[c].append(r)
    for v in wallsbyrow.keys():
        wallsbyrow[v] = sorted(wallsbyrow[v])
    for v in wallsbycol.keys():
        wallsbycol[v] = sorted(wallsbycol[v])
    
    Q = ini()
    for _ in range(Q):
        d, l = mapstr()
        l = int(l)
        if d == "L":
            index = bisect_right(wallsbyrow[curr[0]], curr[1]) - 1
            if index == -1:
                curr[1] = max(1, curr[1]-l)
            else:
                curr[1] = max(wallsbyrow[curr[0]][index]+1, curr[1]-l)
        elif d == "R":
            index = bisect_right(wallsbyrow[curr[0]], curr[1])
            if index >= len(wallsbyrow[curr[0]]):
                curr[1] = min(W, curr[1]+l)
            else:
                curr[1] = min(wallsbyrow[curr[0]][index]-1, curr[1]+l)
        elif d == "U":
            index = bisect_right(wallsbycol[curr[1]], curr[0]) - 1
            if index == -1:
                curr[0] = max(1, curr[0]-l)
            else:
                curr[0] = max(wallsbycol[curr[1]][index]+1, curr[0]-l)
        elif d == "D":
            index = bisect_right(wallsbycol[curr[1]], curr[0])
            if index >= len(wallsbycol[curr[1]]):
                curr[0] = min(H, curr[0]+l)
            else:
                curr[0] = min(wallsbycol[curr[1]][index]-1, curr[0]+l)
        print(*curr)
    
        
        
        
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