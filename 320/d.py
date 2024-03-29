import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    
    d = defaultdict(list)
    for _ in range(M):
        a, b, x, y = map(int, input().split())
        d[a].append((b, x, y))
        d[b].append((a, -x, -y))
    
    ans = [(-1,-1)] * (N+1)
    ans[1] = (0,0)
    que = deque([1])
    visited = set([1])
    while que:
        now = que.popleft()
        current_node = ans[now]
        for nxt, x, y in d[now]:
            if nxt in visited:
                continue
            ans[nxt] = (x+current_node[0],y+current_node[1])
            que.append(nxt)
            visited.add(nxt)
    for i in range(1, N+1):
        if ans[i] == (-1,-1):
            print("undecidable")
        else:
            print(ans[i][0], ans[i][1])
        
    

if __name__ == "__main__":
    main()