import heapq

def main():
    N, M = mapint()
    
    x2 = set()
    for i in range(int(pow(M, 1/2)+1)):
        x2.add(i*i)
    d = set()
    for i in range(int(pow(M, 1/2))+1):
        diff = M - i*i
        if diff < i*i:
            break
        if diff in x2:
            d.add((i, int(pow(diff, 1/2))))
            d.add((int(pow(diff, 1/2)), i))
    errprint(d)
    nodes = [[float("inf")] * (N+1) for _ in range(N+1)]
    nodes[1][1] = 0
    # dikstra
    q = []
    heapq.heappush(q, (0, 1, 1))
    while q:
        cost, x, y = heapq.heappop(q)
        for dx, dy in d:
            for direct in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                nx, ny = x+dx*direct[0], y+dy*direct[1]
                if nx < 1 or nx > N or ny < 1 or ny > N:
                    continue
                if nodes[nx][ny] > cost+1:
                    nodes[nx][ny] = cost+1
                    heapq.heappush(q, (cost+1, nx, ny))
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            if nodes[i][j] == float("inf"):
                print(-1, end=" ")
            else:
                print(nodes[i][j], end=" ")
        print()
    
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