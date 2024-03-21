import sys
from collections import deque
input = sys.stdin.readline

def main():
    R, C = map(int, input().split())
    
    start = list(map(int, input().split()))
    goal = list(map(int, input().split()))
    # y x
    
    grid = [list(input().strip()) for _ in range(R)]
    que = deque()
    
    que.append(start)
    
    grid[start[0]-1][start[1]-1] = "0"
    while que:
        y, x = que.popleft()
        if [y, x] == goal:
            print(grid[y-1][x-1])
            return
        for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if grid[y+dy-1][x+dx-1] == ".":
                grid[y+dy-1][x+dx-1] = str(int(grid[y-1][x-1]) + 1)
                que.append([y+dy, x+dx])
    print(grid[goal[0]-1][goal[1]-1])
        
    

if __name__ == "__main__":
    main()