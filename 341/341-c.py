
import sys
input = sys.stdin.readline

def move_node(y, x, s):
    if s == "L":
        return (y, x-1)
    elif s == "R":
        return (y, x+1)
    elif s == "U":
        return (y-1, x)
    elif s == "D":
        return (y+1, x)

def check_node(y, x, grid, T):
    for t in T:
        y, x = move_node(y, x, t)
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid) or grid[y][x] == "#":
            return False
    
    return True
    
def main():
    H, W, N = map(int, input().split())
    T = input().strip()
    grid = [input().strip() for _ in range(H)]
    
    ans = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "#":
                continue
            if check_node(i, j, grid, T):
                ans += 1
    print(ans)

if __name__ == "__main__":
    main()