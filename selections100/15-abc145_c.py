import sys
from itertools import permutations
input = sys.stdin.readline

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def main():
    N = int(input())
    
    edges = []
    for _ in range(N):
        x, y = map(int, input().split())
        edges.append((x, y))
    
    ans = 0
    permutations_list = list(permutations(range(N)))
    for p in permutations_list:
        total = 0
        for i in range(1, N):
            total += distance(edges[p[i]][0], edges[p[i]][1], edges[p[i-1]][0], edges[p[i-1]][1])
        
        ans += total
    print(ans / len(permutations_list))
    
    
        
    
if __name__ == "__main__":
    main()