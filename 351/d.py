def main():
    H, W = mapint()
    
    S = [lstr() for _ in range(H)]
    
    free_node = set()
    for i in range(H):
        for j in range(W):
            if S[i][j] != ".":
                continue
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i+d[0], j+d[1]
                if not (0 <= ni < H and 0 <= nj < W):
                    continue
                if S[ni][nj] == "#":
                    break
            else:
                free_node.add((i, j))
    ans = 0
    if not free_node:
        print(1)
        return
    free_visited = set()
    for i, j in free_node:
        if (i, j) in free_visited:
            continue
        free_visited.add((i, j))
        # dfs
        visited = set()
        stack = [(i, j)]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            x, y = node
            if node in free_node:
                free_visited.add(node)
                for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x+d[0], y+d[1]
                    if not (0 <= nx < H and 0 <= ny < W):
                        continue
                    stack.append((nx, ny))
        ans = max(ans, len(visited))
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