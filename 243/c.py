from collections import defaultdict

def main():
    N = ini()
    nodes = [lint() for _ in range(N)]
    S = lstr()
    
    y_grid_nodesL = defaultdict(int)
    y_grid_nodesR = defaultdict(lambda: 10**9+1)
    for i in range(N):
        x, y = nodes[i]
        s = S[i]
        if s == "L":
            y_grid_nodesL[y] = max(y_grid_nodesL[y], x)
        elif s == "R":
            y_grid_nodesR[y] = min(y_grid_nodesR[y], x)
    
    for y in y_grid_nodesL.keys():
        leftX = y_grid_nodesL[y]
        rightX = y_grid_nodesR[y]
        if leftX >= rightX:
            print("Yes")
            return
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