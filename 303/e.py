from collections import defaultdict

def main():
    N = ini()
    
    edges = defaultdict(list)
    for _ in range(N-1):
        a, b = mapint()
        edges[a].append(b)
        edges[b].append(a)
    
    numEdgesOfNode = [0] * (N+1)
    for k, v in edges.items():
        numEdgesOfNode[k] = len(v)
    
    sortedNodes = sorted(range(1, N+1), key=lambda x: numEdgesOfNode[x], reverse=True)
    # errprint(numEdgesOfNode)
    # errprint(sortedNodes)
    ans = []
    visited = set()
    restNodes = 0
    for i in sortedNodes:
        if numEdgesOfNode[i] > 2:
            ans.append(numEdgesOfNode[i])
            visited.add(i)
            for e in edges[i]:
                visited.add(e)
        else:
            if i in visited:
                continue
            restNodes += 1
    
    for _ in range(restNodes//3):
        ans.append(2)

    print(*(ans[::-1]))

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