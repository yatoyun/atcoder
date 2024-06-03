from copy import deepcopy
from collections import deque

def main():
    P = []
    cnt = 0
    for _ in range(3):
        tmp = [lstr() for _ in range(4)]
        polyomino = []
        first = None
        for i in range(4):
            for j in range(4):
                if tmp[i][j] == "#":
                    if first is None:
                        first = (i, j)
                        polyomino.append((0, 0))
                    else:
                        polyomino.append((i-first[0], j-first[1]))
                    cnt += 1
        P.append(polyomino)
    if cnt != 16:
        print("No")
        return
    P.sort(key=lambda x: len(x), reverse=True)
    
    def rotate(polyomino):
        return [(y, -x) for x, y in polyomino]
    
    que = deque()
    
    p = P[0]
    for j in range(len(p)):
        curr = (0, 0)
        for _ in range(4):
            tmp = [[0]*4 for _ in range(4)]
            tmp[0][0] = 1
            p = rotate(p)
            s = p[j]
            for k in range(len(p)):
                if k == j:
                    continue
                x, u = p[k]
                x -= s[0]
                u -= s[1]
                nx, nu = curr[0]+x, curr[1]+u
                if nx < 0 or nx >= 4 or nu < 0 or nu >= 4:
                    break
                tmp[nx][nu] = 1
            else:
                # success
                break
            # fail
        else:
            continue
        que.append((0, [tmp]))
    # 2-3
    while que:
        index, tmps = que.popleft()
        if index == 2:
            print("Yes")
            return
        curr_p = P[index+1]
        grid = [[0]*4 for _ in range(4)]
        # grid setup
        for tm in tmps:
            for i in range(4):
                for j in range(4):
                    if tm[i][j] == 1:
                        grid[i][j] = 1
                        
        for j in range(len(curr_p)):
            for y in range(4):
                for w in range(4):
                    if grid[y][w] == 1:
                        continue
                    curr = (y, w)
                    p = deepcopy(curr_p)
                    for _ in range(4):
                        p = rotate(p)
                        s = p[j]
                        tmp = [[0]*4 for _ in range(4)]
                        tmp[y][w] = 1
                        for k in range(len(p)):
                            if k == j:
                                continue
                            x, u = p[k]
                            x = x - s[0]
                            u = u - s[1]
                            nx, nu = curr[0]+x, curr[1]+u
                            if nx < 0 or nx >= 4 or nu < 0 or nu >= 4:
                                break
                            if grid[nx][nu] == 1:
                                break
                            tmp[nx][nu] = 1
                        else:
                            # success
                            next_tmps = deepcopy(tmps)
                            next_tmps.append(deepcopy(tmp))
                            que.append((index+1,next_tmps))
                        # fail
                        
    print("No")

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