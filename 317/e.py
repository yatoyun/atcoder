direct = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

def preprocess(H, W, A, grid, di, node):
    y, x = node
    grid[y][x] = -1
    while True:
        ny, nx = di[0]+y, di[1]+x
        if nx<0 or nx>=W or ny<0 or ny>=H:
            return
        if A[ny][nx] == "#" or A[ny][nx] in direct:
            return
        grid[ny][nx] = -1
        y, x = ny, nx
        


def main():
    H, W = mapint()
    A = [lstr() for _ in range(H)]
    
    grid = [[0]*W for _ in range(H)]

    st = None
    g = None
    for i in range(H):
        for j in range(W):
            node =  A[i][j]
            if node == "#":
                grid[i][j] = -1
            elif node == "S":
                st = (i, j)
            elif node == "G":
                g = (i, j)
            elif node in direct:
                preprocess(H, W, A, grid, direct[node], (i, j))

    que = deque()
    que.append(st)
    grid[st[0]][st[1]] = 0
    while que:
        y, x = que.popleft()
        for dx, dy in direct.values():
            ny, nx = y+dy, x+dx
            if nx<0 or nx>=W or ny<0 or ny>=H:
                continue
            if grid[ny][nx] != 0:
                continue
            
            grid[ny][nx] = grid[y][x]+1
            que.append((ny, nx))
    print(grid[g[0]][g[1]] if grid[g[0]][g[1]] != 0 else -1)
    
            
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
    from collections import deque
    input = sys.stdin.readline
    atcenv = os.environ.get("ATCODER", 0)

    main()