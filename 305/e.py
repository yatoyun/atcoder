from collections import defaultdict, deque
import heapq as hq
def main():
    N, M, K = mapint()
    edges = defaultdict(list)
    
    for _ in range(M):
        a, b = mapint0()
        edges[a].append(b)
        edges[b].append(a)
    
    nodes = [0]*N
    guards = []
    for _ in range(K):
        c, d = mapint()
        guards.append((-(d+1), c-1))
    hq.heapify(guards)
    while guards:
        h, g = hq.heappop(guards)
        h = -h
        if nodes[g] >= h:
            continue
        nodes[g] = h
        for e in edges[g]:
            hq.heappush(guards, (-(h-1), e))
    
    ans = []
    for i in range(N):
        if nodes[i]:
            ans.append(i+1)
    
    print(len(ans))
    print(*ans)
    

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