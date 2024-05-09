from collections import defaultdict

def main():
    N, Q = mapint()
    
    edges = defaultdict(set)
    
    total_isolated = N
    for _ in range(Q):
        query = lint()
        if query[0] == 1:
            u, v = query[1:]
            minus = 0
            if len(edges[u]) == 0:
                minus += 1
            if len(edges[v]) == 0:
                minus += 1
            edges[u].add(v)
            edges[v].add(u)
            total_isolated -= minus
        else:
            v = query[1]
            for u in edges[v]:
                edges[u].remove(v)
                if len(edges[u]) == 0:
                    total_isolated += 1
            if len(edges[v]) != 0:
                del edges[v]
                total_isolated += 1
        print(total_isolated)

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