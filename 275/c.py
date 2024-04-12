def main():
    S = [lstr() for _ in range(9)]
    
    porns = set()
    for i in range(9):
        for j in range(9):
            if S[i][j] == "#":
                porns.add((i,j))
    
    ans = 0
    for porn in porns:
        y, x = porn
        for nxtporn in porns:
            if porn == nxtporn:
                continue
            dy = nxtporn[0] - y
            dx = nxtporn[1] - x
            
            if dy < 0 or dx <= 0 or x-dy < 0 or y+dy+dx >= 9:
                continue
            errprint(porn, nxtporn)
            if (y+dx, x-dy) not in porns:
                continue
            if (y+dy+dx, x+dx-dy) not in porns:
                continue
            ans += 1
            errprint(ans)
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