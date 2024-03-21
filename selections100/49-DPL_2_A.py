import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    V, E = map(int, input().split())
    
    Edges = defaultdict(lambda: float("inf"))
    for _ in range(E):
        s, t, d = map(int, input().split())
        Edges[(s,t)] = d
    
    dp = [[float("inf")] * V for _ in range(1 << V)]
    
    dp[1][0] = 0  # 集合{0}で、現在地が0の状態
    for visited in range(1 << V):
        for last in range(V):
            if dp[visited][last] == float("inf"):
                continue
            for nxt in range(V):
                if visited & (1 << nxt) or Edges[(last, nxt)] == float("inf"):
                    continue
                dp[visited | (1 << nxt)][nxt] = min(dp[visited | (1 << nxt)][nxt], dp[visited][last] + Edges[(last, nxt)])
    
    ans = min([float("inf"),*[dp[(1 << V) - 1][last] + Edges[(last, 0)] for last in range(1, V) if Edges[(last, 0)] != float("inf")]])
    
    if ans == float("inf"):
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    main()

