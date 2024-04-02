from collections import defaultdict, deque

def main():
    N, M = mapint()
    A = lint()
    B = lint()
    
    grid = defaultdict(set)
    nodes = dict()
    
    for i in range(M):
        grid[A[i]].add(B[i])
        grid[B[i]].add(A[i])

    for a in set(A):
        if a in nodes:
            continue
        nodes[a] = 1
        que = deque()
        que.append(a)
        while que:
            cu = que.popleft()
            cu_val = nodes[cu]
            for nx in grid[cu]:
                if nx in nodes:
                    if cu_val == nodes[nx]:
                        print("No")
                        return
                    continue
                nodes[nx] = 0 if cu_val == 1 else 1
                que.append(nx)
    print("Yes")
    

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