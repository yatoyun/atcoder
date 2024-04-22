from collections import defaultdict
def main():
    H, W, M = mapint()
    orders = []
    for i in range(M):
        t, a, x = mapint()
        orders.append((t, a, x))
    
    colors = defaultdict(int)
    row = set()
    col = set()
    total = 0
    max_color = 0
    for order in orders[::-1]:
        t, a, x = order
        if t == 1:
            if a in row:
                continue
            row.add(a)
            colors[x] += W - len(col)
            total += W - len(col)
        else:
            if a in col:
                continue
            col.add(a)
            colors[x] += H - len(row)
            total += H - len(row)
        max_color = max(max_color, x)
    colors[0] = H*W - total + colors[0]
    num_color = 0
    for i in range(max_color+1):
        if colors[i] == 0:
            continue
        num_color += 1
    print(num_color)
    for i in range(max_color+1):
        if colors[i] == 0:
            continue
        print(i, colors[i])
    

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