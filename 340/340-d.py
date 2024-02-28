
import sys
input = sys.stdin.readline
import heapq

def main():
    N = int(input())
    graph = []
    for _ in range(N-1):
        graph.append(list(map(int, input().split())))
    
    nodes = []
    heapq.heappush(nodes, (0, 0)) # (cost, node)
    costs = {i: float('inf') for i in range(N)}
    costs[0] = 0
    
    while nodes:
        cost, node = heapq.heappop(nodes)
        if node == N-1:
            continue
        a, b, x = graph[node]
        if costs[node+1] > costs[node] + a:
            costs[node+1] = costs[node] + a
            heapq.heappush(nodes, (costs[node+1], node+1))
        
        if costs[x-1] > costs[node] + b:
            costs[x-1] = costs[node] + b
            heapq.heappush(nodes, (costs[x-1], x-1))
    
    print(costs[N-1])

if __name__ == "__main__":
    main()
