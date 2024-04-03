def count(x, y, dx, dy, C, cnt):
    nx, ny = x+dx, y+dy
    if nx<0 or nx>=len(C) or ny<0 or ny>=len(C[0]):
        return cnt
    if C[nx][ny]==".":
        return cnt
    return count(nx, ny, dx, dy, C, cnt+1)

def main():
    H, W = mapint()
    N = min(H, W)
    C = [lstr() for _ in range(H)]
    
    ans = [0]*(N+1)
    for i in range(1, H-1):
        for j in range(1, W-1):
            if C[i][j]==".":
                continue
            min_cnt = N+1
            for d in [(1,1), (1,-1), (-1,1), (-1,-1)]:
                cnt = count(i, j, d[0], d[1], C, 0)
                min_cnt = min(min_cnt, cnt)
            ans[min_cnt] += 1
            errprint(i, j, min_cnt)
    print(*ans[1:])

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