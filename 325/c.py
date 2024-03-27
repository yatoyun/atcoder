import sys
input = sys.stdin.readline

def dfs(y, x, visited, graph):
    stack = [(y, x)]
    while stack:
        y, x = stack.pop()
        dx = [0, 1, -1]
        dy = [0, 1, -1]
        for i in range(3):
            for j in range(3):
                if i == 0 and j == 0:
                    continue
                nx = x + dx[i]
                ny = y + dy[j]
                if 0 <= nx < len(graph[0]) and 0 <= ny < len(graph):
                    if graph[ny][nx] == "#" and (ny, nx) not in visited:
                        visited.add((ny, nx))
                        stack.append((ny, nx))

def main():
    H, W = map(int, input().split())
    graph = [list(input().strip()) for _ in range(H)]
    
    visited = set()
    count = 0
    for i in range(H):
        for j in range(W):
            if graph[i][j] == "#" and (i, j) not in visited:
                visited.add((i, j))
                dfs(i, j, visited, graph)
                count += 1
    print(count)
    

if __name__ == "__main__":
    main()
