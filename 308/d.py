def main():
    snuke = "snuke"
    
    H, W = mapint()
    S = [lstr() for _ in range(H)]
    
    stack = [(0, 0, 0)]
    visited = set()
    while stack:
        h, w, t = stack.pop()
        if S[h][w] != snuke[t%5]:
            continue
        visited.add((h, w))
        # errprint(h, w, t, S[h][w])
        if h == H-1 and w == W-1:
            print("Yes")
            return
        for dh, dw in [(0,1),(0,-1),(1,0),(-1,0)]:
            nh, nw = h+dh, w+dw
            if nh < 0 or nh >= H or nw < 0 or nw >= W:
                continue
            if (nh, nw) in visited:
                continue
            stack.append((nh, nw, t+1))
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