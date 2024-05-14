def main():
    H, W = mapint()
    
    C = [lstr() for _ in range(H)]
    
    for i in range(H):
        for j in range(W):
            if C[i][j] == "S":
                st = (i, j)
    
    visited = set()
    stack = [(0, st)] # cost, node
    while stack:
        cost, node = stack.pop()
        if node in visited:
            if node == st and cost >= 4:
                print("Yes")
                exit()
            continue
        visited.add(node)
        i, j = node
        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= ni < H and 0 <= nj < W and C[ni][nj] != "#":
                stack.append((cost+1, (ni, nj)))
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