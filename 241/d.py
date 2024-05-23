from sortedcontainers import SortedList
def main():
    Q = ini()
    s = SortedList()
    
    for _ in range(Q):
        q, *a = mapint()
        if q == 1:
            x = a[0]
            s.add(x)
        elif q == 2:
            x, k = a
            index = s.bisect_right(x) -1
            if index+1 < k:
                print(-1)
                continue
            print(s[index-k+1])
        else:
            x, k = a
            index = s.bisect_left(x)
            if len(s)-index < k:
                print(-1)
                continue
            print(s[index+k-1])

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