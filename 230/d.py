from bisect import bisect_left, bisect_right
from sortedcontainers import SortedList

def key_func(x):
    if type(x)==int:
        return x
    return x[1]

def main():
    N, D = mapint()
    ranges = [tuple(lint()) for _ in range(N)]
    ranges_right = SortedList(ranges, key=key_func)
    ranges.sort()
    ranges_left = [x[0] for x in ranges]
    
    index = 0
    cnt = 0
    while index < N:
        curr_right = ranges_right[0][1]
        new_index = bisect_right(ranges_left, curr_right+D-1)
        # remove
        for i in range(index, new_index):
            ranges_right.remove(ranges[i])
        cnt += 1
        index = new_index
    print(cnt)
        

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