def main():
    N, D = mapint()
    ranges = [lint() for _ in range(N)]
    ranges.sort(key=lambda x: x[1])
    
    index = 0
    x = -10**10
    cnt = 0
    while index < N:
        l, r = ranges[index]
        if x+D-1 < l:
            x = r
            cnt += 1
        index += 1
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