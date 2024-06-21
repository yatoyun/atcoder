from sortedcontainers import SortedDict
def main():
    Q = ini()
    
    sd = SortedDict()
    for _ in range(Q):
        query = lint()
        if query[0] == 1:
            x = query[1]
            if x in sd:
                sd[x] += 1
            else:
                sd[x] = 1
        elif query[0] == 2:
            x, c = query[1], query[2]
            if x not in sd:
                continue
            currernt = sd[x]
            sd[x] -= min(currernt, c)
            if sd[x] == 0:
                del sd[x]
        else:
            max_key = sd.peekitem(-1)[0]
            min_key = sd.peekitem(0)[0]
            print(max_key-min_key)

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