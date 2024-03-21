import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs(vertices, Edge):
    stack = [1]
    visited = set([1])
    while stack:
        v = stack.pop()
        for u in Edge[v]:
            if u in visited:
                continue
            vertices[u] += vertices[v]
            visited.add(u)
            stack.append(u)

def main():
    N, Q = map(int, input().split())
    Edge = defaultdict(list)
    vertices = [0] * (N+1)
    for _ in range(N-1):
        a, b = map(int, input().split())
        Edge[a].append(b)
        Edge[b].append(a)
    
    for _ in range(Q):
        p, x = map(int, input().split())
        vertices[p] += x
    
    dfs(vertices, Edge)
    print(*vertices[1:])

if __name__ == "__main__":
    main()