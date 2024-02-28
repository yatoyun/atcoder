import sys
input = sys.stdin.readline

def change_direction(dx, dy, normal):
    if normal:
        if dx == 0 and dy == -1:
            dx = 1
            dy = 0
        elif dx == 1 and dy == 0:
            dx = 0
            dy = 1
        elif dx == 0 and dy == 1:
            dx = -1
            dy = 0
        elif dx == -1 and dy == 0:
            dx = 0
            dy = -1
    else:       
        if dx == 0 and dy == -1:
            dx = -1
            dy = 0
        elif dx == 1 and dy == 0:
            dx = 0
            dy = -1
        elif dx == 0 and dy == 1:
            dx = 1
            dy = 0
        elif dx == -1 and dy == 0:
            dx = 0
            dy = 1
    return dx, dy

def main():
    H, W, N = map(int, input().split())
    
    grid = [["." for _ in range(W)] for _ in range(H)]
    
    dx = 0
    dy = -1
    
    cu_x = 0
    cu_y = 0
    
    for _ in range(N):
        if "." == grid[cu_y][cu_x]:
            dx, dy = change_direction(dx, dy, True)
            grid[cu_y][cu_x] = "#"
        else:
            dx, dy = change_direction(dx, dy, False)
            grid[cu_y][cu_x] = "."
        
        cu_x += dx
        cu_y += dy
        
        if cu_x == -1:
            cu_x = W - 1
        elif cu_x == W:
            cu_x = 0
        
        if cu_y == -1:
            cu_y = H - 1
        elif cu_y == H:
            cu_y = 0
        

    # print grid
    for i in range(H):
        for j in range(W):
            print(grid[i][j], end="")
        print()


if __name__ == "__main__":
    main()