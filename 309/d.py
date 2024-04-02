from collections import defaultdict, deque

def get_max_dim(edges, st_node):
    que = deque([(st_node,0)])
    visited = set()
    max_dim = 0
    
    while que:
        node, cu_dim = que.popleft()
        visited.add(node)
        max_dim = max(max_dim, cu_dim)
        for next_node in edges[node]:
            if next_node in visited:
                continue
            que.append((next_node, cu_dim+1))
            visited.add(next_node)
    return max_dim

def main():
    N1, N2, M = mapint()
    edges = defaultdict(list)
    
    for _ in range(M):
        a, b = mapint0()
        edges[a].append(b)
        edges[b].append(a)
    errprint(edges)
    max_dim1 = get_max_dim(edges, 0)
    max_dim2 = get_max_dim(edges, N1+N2-1)
    print(max_dim1+max_dim2+1)
    

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