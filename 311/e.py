def main():
    H, W, N = mapint()
    grid = [[1] * W for _ in range(H)]
    for _ in range(N):
        a, b = mapint0()
        grid[a][b] = 0
    
    ans = 0
    for i in range(H):
        for j in range(W):
            def get_count(i, j):
                if grid[i][j] == 0:
                    return 0
                min_x = float("inf")
                for d in [(-1,0),(0,-1),(-1,-1)]:
                    ni = i+d[0]
                    nj = j+d[1]
                    if not(0<=ni<H and 0<=nj<W) or grid[ni][nj] == 0:
                        return 1
                    min_x = min(min_x, grid[ni][nj])
                return min_x+1
            grid[i][j] = get_count(i, j)
            ans += grid[i][j]
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