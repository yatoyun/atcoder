from bisect import bisect_left, bisect_right
from collections import defaultdict
def main():
    W, H = mapint()
    N = ini()
    strawberries = []
    for _ in range(N):
        p, q = mapint()
        strawberries.append((p, q))
    A = ini()
    a_list = [0, *lint(), W]
    B = ini()
    b_list = [0, *lint(), H]
    
    max_cnt = 0
    node_dict = defaultdict(int)
    for st in strawberries:
        row_ed = bisect_right(a_list, st[0])
        col_ed = bisect_right(b_list, st[1])
        node_dict[(col_ed-1, row_ed-1)] += 1
        max_cnt = max(max_cnt, node_dict[(col_ed-1,row_ed-1)])
    min_cnt = min(node_dict.values()) if len(node_dict) == (A+1)*(B+1) else 0
    print(min_cnt, max_cnt)

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