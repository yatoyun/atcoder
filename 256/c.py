def main():
    X = lint()
    h = X[:3]
    w = X[3:]
    
    def update_grid(grid, nums):
        idx = 0
        for i in range(2):
            for j in range(2):
                grid[i][j] = nums[idx]
                idx += 1
        return grid
    
    def update_h3(grid):
        for i in range(2):
            grid[i][2] = h[i] - sum(grid[i][j] for j in range(2))
            if grid[i][2] <= 0:
                return False
        return True

    def update_w3(grid):
        for i in range(2):
            grid[2][i] = w[i] - sum(grid[j][i] for j in range(2))
            if grid[2][i] <= 0:
                return False
        return True
    
    def update_last(grid):
        grid[2][2] = h[2] - sum(grid[2][j] for j in range(2))
        if grid[2][2] <= 0:
            return False
        if sum(grid[i][-1] for i in range(3)) != w[-1]:
            return False
        return True
    
    cnt = 0
    grid = [[1]*3 for _ in range(3)]
    stack = [[]]
    while stack:
        nums = stack.pop()
        if len(nums) < 4:
            for x in range(1, 29):
                stack.append(nums+[x])
            continue
        grid = update_grid(grid, nums)
        if not update_h3(grid):
            continue
        if not update_w3(grid):
            continue
        if not update_last(grid):
            continue
        cnt += 1
    print(cnt)


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
