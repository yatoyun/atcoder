def main():
    N, M = mapint()
    grid = [lstr() for _ in range(N)]
    
    visited = set()
    visited_pass = set([(1,1)])
    stack = [(1,1)]
    while stack:
        y, x = stack.pop()
        if (y, x) in visited or grid[y][x] == "#":
            continue
        visited.add((y, x))
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            cu_x = x
            cu_y = y
            while True:
                nu_y, nu_x = cu_y+dy, cu_x+dx
                if grid[nu_y][nu_x] == "#":
                    stack.append((cu_y, cu_x))
                    break
                visited_pass.add((nu_y, nu_x))
                cu_y = nu_y
                cu_x = nu_x
    print(len(visited_pass))

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