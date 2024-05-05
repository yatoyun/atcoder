from collections import defaultdict, deque

def main():
    N = ini()
    edges = defaultdict(list)
    
    for i in range(N):
        P = lint0()
        edges[i] = P[1:]
    
    # topological sort
    indegree = [0]*N
    for i in range(N):
        for e in edges[i]:
            indegree[e] += 1
    
    que = deque([i for i in range(N) if indegree[i] == 0])
    order = []
    while que:
        node = que.popleft()
        for e in edges[node]:
            indegree[e] -= 1
            if indegree[e] == 0:
                que.append(e)
        order.append(node+1)

    st = deque()
    st.append(0)
    nodes = set()
    while st:
        node = st.popleft()
        if (node+1) in nodes:
            continue
        nodes.add(node+1)
        for e in edges[node]:
            st.append(e)
    nodes.remove(1)
    
    ans = []
    for node in order[::-1]:
        if node in nodes:
            ans.append(node)
    print(*ans)
    

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