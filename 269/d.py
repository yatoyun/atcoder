D = [(-1,-1), (-1,0), (0,-1), (0,1), (1,0), (1,1)]

def main():
    N = ini()
    nodes = set()
    for _ in range(N):
        x, y = mapint()
        nodes.add((x, y))
    
    ans = 0
    visited = set()
    for x, y in nodes:
        if (x, y) in visited:
            continue
        stack = []
        stack.append((x, y))
        while stack:
            x, y = stack.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for d in D:
                nx, ny = x+d[0], y+d[1]
                if (nx, ny) in nodes:
                    stack.append((nx, ny))
        ans += 1
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