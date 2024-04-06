def main():
    N = ini()
    nodes = []
    for _ in range(N):
        x, y = mapint()
        nodes.append((x, y))
    
    for i in range(N):
        x, y = nodes[i]
        max_dist = 0
        ans = 0
        for j in range(N):
            if i==j:
                continue
            xx, yy = nodes[j]
            dist = (x-xx)**2 + (y-yy)**2
            if dist>max_dist:
                max_dist = dist
                ans = j
        print(ans+1)

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