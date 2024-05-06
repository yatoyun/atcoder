from  collections import defaultdict, deque
def main():
    N,M = mapint()
    A = lint()
    
    children = defaultdict(list)
    for i in range(2, N+1):
        children[A[i-2]].append(i)
    
    nodes = [0]*(N+1)
    for _ in range(M):
        x, y = mapint()
        nodes[x] = max(nodes[x], y+1)
    
    que = deque()
    que.append((1, nodes[1]))
    ans = 0
    while que:
        errprint(que)
        now, cnt = que.popleft()
        if cnt > 0:
            cnt -= 1
            ans += 1
        for c in children[now]:
            que.append((c, max(cnt, nodes[c])))
    
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