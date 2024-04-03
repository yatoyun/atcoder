def main():
    N, M, H, K = mapint()
    d = {"R":(1,0), "L":(-1,0), "U":(0,1), "D":(0,-1)}
    S = lstr()
    heal = set()
    for i in range(M):
        x, y = mapint()
        heal.add((x,y))
    
    cur = (0,0)
    hp = H
    for s in S:
        dx, dy = d[s]
        cur = (cur[0]+dx, cur[1]+dy)
        hp -= 1
        if hp<0:
            print("No")
            return
        if hp < K and cur in heal:
            heal.remove(cur)
            hp = K
        errprint(cur, hp)
    print("Yes")

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