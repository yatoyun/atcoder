from collections import defaultdict
import heapq as hq
def main():
    N, M, K = mapint()
    
    edges = [defaultdict(list) for _ in range(2)]
    
    for _ in range(M):
        v, u, a = mapint()
        edges[a][v].append(u)
        edges[a][u].append(v)
    
    switch = set(lint())
    
    dist = [[float("inf")]*(N+1) for _ in range(2)]
    
    que = [(0, 1, 1)]
    hq.heapify(que)
    while que:
        d, v, a = hq.heappop(que)
        if dist[a][v] <= d or dist[0][-1] <= d or dist[1][-1] <= d:
            continue
        dist[a][v] = d
        if v in switch:
            hq.heappush(que, (d, v, 1-a))
        for u in edges[a][v]:
            hq.heappush(que, (d+1, u, a))
    
    ans = min(dist[0][-1], dist[1][-1])
    print(ans if ans != float("inf") else -1)

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