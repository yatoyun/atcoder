from bisect import bisect_left, bisect_right
from collections import defaultdict
def main():
    N = ini()
    
    nums = defaultdict(int)
    AC = []
    for i in range(N):
        a, c = mapint()
        AC.append((a, c))
        nums[(a, c)] = i
    
    AC.sort(key=lambda x: x[0], reverse=True)
    C = [c for a, c in AC]
    C.sort()
    non_set = set()
    ans = []
    ex_index = len(C)
    for a, c in AC:
        if c in non_set:
            continue
        ans.append(nums[(a, c)]+1)
        index = bisect_right(C, c)
        if ex_index < index:
            continue
        for i in range(index, ex_index):
            non_set.add(C[i])
        ex_index = index
    
    ans.sort()
    print(len(ans))
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