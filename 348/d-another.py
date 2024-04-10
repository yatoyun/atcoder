from collections import defaultdict, deque
def main():
    H, W = mapint()
    A = []
    for i in range(H):
        ls = lstr()
        if "S" in ls:
            start = (i, ls.index("S"))
        if "T" in ls:
            end = (i, ls.index("T"))
        A.append(ls)
    N = ini()
    heal_dict = {}
    heal_nodes = []
    heal_index = {}
    for i in range(N):
        r, c, e = mapint0()
        heal_dict[(r, c)] = e
        heal_nodes.append((r, c))
        heal_index[(r, c)] = i
    if start not in heal_dict:
        print("No")
        return
    
    def bfs(st, heal):
        que = deque([st])
        dist = [[-1]*W for _ in range(H)]
        dist[st[0]][st[1]] = 0
        while que:
            p = que.popleft()

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                np = (p[0]+dx, p[1]+dy)
                if np[0]<0 or np[0]>=H or np[1]<0 or np[1]>=W: continue
                if A[np[0]][np[1]] == "#": continue
                if dist[np[0]][np[1]] != -1: continue
                dist[np[0]][np[1]] = dist[p[0]][p[1]]+1
                if dist[np[0]][np[1]] > heal: continue
                que.append(np)
        return dist
    
    heal_edges = defaultdict(list)
    if end not in heal_dict:
        heal_nodes.append(end)
        heal_index[end] = N
    for i in range(len(heal_nodes)-1):
        all_dist = bfs(heal_nodes[i], heal_dict.get(heal_nodes[i], 0))
        for j in range(len(heal_nodes)):
            if i == j: continue
            dist = all_dist[heal_nodes[j][0]][heal_nodes[j][1]]
            if dist == -1: continue
            heal_edges[i].append(j)
    errprint(heal_nodes)
    errprint(heal_index)
    que = deque([heal_index[start]])
    visited = [-1]*len(heal_nodes)
    while que:
        p = que.popleft()
        if visited[p] != -1: continue
        visited[p] = 1
        if p == heal_index[end]:
            print("Yes")
            return
        for nex in heal_edges[p]:
            que.append(nex)
    errprint(visited)
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