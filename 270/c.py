from collections import defaultdict

def main():
    N, st, ed = mapint()
    edges = defaultdict(list)
    
    for i in range(1, N):
        u, v = mapint()
        edges[u].append(v)
        edges[v].append(u)
    
    nodes = defaultdict(int)
    visited = set()
    stack = [st]
    nodes[st] = -1
    visited.add(st)
    while stack:
        now = stack.pop()
        if now == ed:
            break
        for nxt in edges[now]:
            if nxt in visited:
                continue
            stack.append(nxt)
            nodes[nxt] = now
            visited.add(nxt)
    ans = []
    while ed != -1:
        ans.append(ed)
        ed = nodes[ed]
    print(*ans[::-1])
            
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