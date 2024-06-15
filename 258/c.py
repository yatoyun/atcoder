def main():
    N, Q = mapint()
    S = lstr()

    st_idx = 0
    for _ in range(Q):
        query, x = mapint()
        if query == 1:
            st_idx = (st_idx - x) % N
        elif query == 2:
            print(S[(st_idx + x - 1) % N])

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