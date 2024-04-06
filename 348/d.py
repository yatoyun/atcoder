from collections import defaultdict, deque
from heapq import heappush, heappop

def main():
    H, W = mapint()
    A = []
    for i in range(H):
        ls = lstr()
        if "S" in ls:
            start = (i, ls.index("S"))
        if "T" in ls:
            end = (i, ls.index("T"))
        A.append(ls)
    N = ini()
    heal_dict = defaultdict(int)
    for _ in range(N):
        r, c, e = mapint0()
        heal_dict[(r, c)] = e+1

    if start not in heal_dict:
        print("No")
        return
    dist = defaultdict(lambda: -1)
    dist[start] = heal_dict[start]
    hq = [(dist[start]*-1, (start))] # (distance, node)
    errprint(end)
    while hq:
        ee, v = heappop(hq) # node
        errprint(v, ee)
        if v == end:
            print("Yes")
            return
        ee *= -1
        if ee <= 0:
            continue
        if dist[v] > ee:
            continue
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = v[0]+dx, v[1]+dy
            if nx<0 or nx>=H or ny<0 or ny>=W:
                continue
            if A[nx][ny]=="#":
                continue
            heal = heal_dict[(nx, ny)]
            c_dist = max(ee-1, heal)
            if c_dist <= dist[(nx, ny)]:
                continue
            heappush(hq, (c_dist*-1, (nx, ny)))
            dist[(nx, ny)] = c_dist
    
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