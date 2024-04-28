import heapq as hq

def main():
    N, A, B, C = mapint()
    D = [lint() for _ in range(N)]
    
    nodes = [float("inf")]*N
    # diskstra
    que = [(0, 0)]
    while que:
        cost, node = hq.heappop(que)
        if nodes[node] <= cost:
            continue
        nodes[node] = cost
        for i in range(1,N):
            if node == i:
                continue
            
            # car
            next_cost = cost + A*D[node][i]
            if nodes[i] > next_cost:
                hq.heappush(que, (next_cost, i))
    ans = nodes[-1]
    new_nodes = [float("inf")]*N
    que = [(v, i) for i, v in enumerate(nodes)]
    hq.heapify(que)
    while que:
        cost, node = hq.heappop(que)
        if new_nodes[node] <= cost:
            continue
        new_nodes[node] = cost
        for i in range(1,N):
            if node == i:
                continue
            # train
            next_cost = cost + B*D[node][i] + C
            if new_nodes[i] > next_cost:
                hq.heappush(que, (next_cost, i))
    ans = min(ans, new_nodes[-1])
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