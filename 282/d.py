from collections import defaultdict

def main():
    N, M = mapint()
    edges = defaultdict(list)

    num_edges = 0
    for _ in range(M):
        a, b = mapint0()
        edges[a].append(b)
        edges[b].append(a)
        num_edges += 1
    
    visited = set()
    white_list = []
    black_list = []
    for node in range(N):
        white = set()
        black = set()
        white.add(node)
        stack = [node]
        while stack:
            node = stack.pop()
            is_white = node in white
            if node in visited:
                continue
            visited.add(node)
            for next_node in edges[node]:
                if is_white:
                    black.add(next_node)
                else:
                    white.add(next_node)
                stack.append(next_node)
        white_list.append(len(white))
        black_list.append(len(black))
        if white & black:
            print(0)
            return
    ans = N * (N-1) // 2
    for node in range(N):
        ans -= white_list[node] * (white_list[node] - 1) // 2
        ans -= black_list[node] * (black_list[node] - 1) // 2
    print(ans - num_edges)

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