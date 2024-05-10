from collections import defaultdict
def main():
    N, M = mapint()
    
    edges = defaultdict(list)
    nodes = [0]*N
    
    for _ in range(M):
        x, y = mapint0()
        edges[x].append(y)
        nodes[y] += 1
    
    head = None
    for i in range(N):
        if nodes[i]==0:
            if head is not None:
                print("No")
                return
            head = i
    if head is None:
        print("No")
        return
    que = [head]
    ans = [head]
    while que:
        now = que.pop()
        min_v = float("inf")
        for nxt in edges[now]:
            if min_v > nodes[nxt]:
                min_v = nodes[nxt]
                min_n = nxt
            nodes[nxt] -= 1
        if min_v==float("inf"):
            continue
        que.append(min_n)
        ans.append(min_n)
    if len(ans)==N:
        print("Yes")
        nums = sorted(range(1,N+1), key=lambda x: ans[x-1])
        print(*nums)
    else:
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