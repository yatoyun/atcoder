def rec(N, grid, x, y):
    if N == 0:
        grid[x][y] = "#"
        return

    distance = 3**(N-1)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            rec(N-1, grid, x+i*distance, y+j*distance)


def main():
    N = ini()

    grid = [["."]*(3**N) for _ in range(3**N)]
    rec(N, grid, 0, 0)
    for i in range(3**N):
        print("".join(grid[i]))

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