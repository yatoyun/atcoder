def get_grid():
    h, w = mapint()
    grid = [lstr() for _ in range(h)]
    return grid

def get_nodes(grid):
    h = len(grid)
    w = len(grid[0])
    nodes = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "#":
                if len(nodes) == 0:
                    st = (i, j)
                nodes.append((i-st[0], j-st[1]))
    return nodes

def main():
    A = get_grid()
    B = get_grid()
    X = get_grid()
    
    A_nodes = get_nodes(A)
    B_nodes = get_nodes(B)
    X_nodes = set(get_nodes(X))
    
    eligible_nodesA = []
    # A
    for st in X_nodes:
        stx, sty = st
        matched_nodes = set()
        for a in A_nodes:
            ax, ay = a
            nx, ny = ax+stx, ay+sty
            if (nx, ny) in X_nodes:
                matched_nodes.add((nx, ny))
            else:
                break
        else:
            eligible_nodesA.append(matched_nodes)
    
    # B
    eligible_nodesB = []
    for st in X_nodes:
        stx, sty = st
        matched_nodes = set()
        for b in B_nodes:
            bx, by = b
            nx, ny = bx+stx, by+sty
            if (nx, ny) in X_nodes:
                matched_nodes.add((nx, ny))
            else:
                break
        else:
            eligible_nodesB.append(matched_nodes)
    
    # Check
    for nodes_setA in eligible_nodesA:
        for nodes_setB in eligible_nodesB:
            if X_nodes == nodes_setA | nodes_setB:
                print("Yes")
                return
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