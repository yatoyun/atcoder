from collections import defaultdict
def main():
    N = ini()
    edges = defaultdict(list)
    
    for _ in range(N-1):
        a, b = mapint()
        edges[a].append(b)
        edges[b].append(a)
    
    # 帰りがけ
    stack = [-1, 1]
    visited = set()
    
    nums = [(float("inf"), -float("inf")) for _ in range(N+1)]
    v = 1
    while stack:
        node = stack.pop()
        if node > 0:
            if node in visited:
                continue
            visited.add(node)
            for n in edges[node]:
                if n in visited:
                    continue
                stack.append(-n)
                stack.append(n)
        else:
            node = -node
            if len(edges[node]) == 1 and node != 1:
                nums[node] = (v, v)
                v += 1
                continue
            if nums[node] != (float("inf"), -float("inf")):
                continue
            min_v = min([nums[n][0] for n in edges[node]])
            max_v = max([nums[n][1] for n in edges[node]])
            nums[node] = (min_v, max_v)
    
    for i in range(1, N+1):
        print(*nums[i])
            

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