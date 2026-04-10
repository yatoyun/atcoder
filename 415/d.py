from bisect import bisect_left, bisect_right

def main():
    N, M = mapint()
    shops = []
    for _ in range(M):
        a, b = mapint()
        shops.append((a, a-b))
    shops.sort(key=lambda x: x[1])

    cur = N
    cnt = 0
    for a, b in shops:
        if a > cur:
            continue
        x = (cur - a) // b + 1
        cur -= x * b
        cnt += x
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