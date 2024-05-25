from collections import defaultdict

def main():
    n, q = mapint()
    X = lint()
    edges = defaultdict(list)
    for _ in range(n-1):
        a, b = mapint()
        edges[a].append(b)
        edges[b].append(a)
    
    nums_maxs = [[] for _ in range(n+1)]
    stack = [-1, 1]
    visited = set()
    while stack:
        node = stack.pop()
        if node > 0:
            visited.add(node)
            for nxt in edges[node]:
                if nxt == node:
                    continue
                if nxt in visited:
                    continue
                stack.append(-nxt)
                stack.append(nxt)
        else:
            node = -node
            if len(edges[node]) == 1 and node != 1:
                nums_maxs[node] = [X[node-1]]
                continue
            # add children to parent
            next_arr = [X[node-1]]
            for child in edges[node]:
                next_arr.extend(nums_maxs[child])
            next_arr.sort()
            nums_maxs[node] = next_arr[-20:]
    
    for _ in range(q):
        v, k = mapint()
        ans = nums_maxs[v][-k]
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