import sys
from itertools import permutations
input = sys.stdin.readline

def main():
    max_cost = 0
    
    N, M = map(int, input().split())
    
    # n * n adj matrix
    adj = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        adj[a][b] = c
        adj[b][a] = c
    
    # bit combination
    for order_list in permutations(range(1, N+1), N):
        batch_max = 0
        count = 0
        current = order_list[0]
        for city in order_list[1:]:
                if adj[current][city] == 0:
                    if batch_max < count:
                        batch_max = count
                    count = 0
                else:
                    count += adj[current][city]
                    current = city
        if batch_max < count:
            batch_max = count
        if max_cost < batch_max:
            max_cost = batch_max
    
    print(max_cost)
                
                
        
        

if __name__ == "__main__":
    main()