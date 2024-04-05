def main():
    N, A, B = mapint()
    S = lstr()
    
    ans = float("inf")
    for st in range(N):
        cost = A*st
        for i in range(N//2):
            nx = st + i if st+i < N else st+i-N
            re = st - i-1 if st-i-1 >= 0 else st-i-1+N
            if S[nx] != S[re]:
                cost += B
        ans = min(ans, cost)
    print(ans)

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
