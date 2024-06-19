from bisect import bisect_left, bisect_right
def main():
    N, Q = mapint()
    A = lint()
    A.sort()

    sums = [0]*(N+1)
    for i in range(N):
        sums[i+1] = sums[i] + A[i]
    for _ in range(Q):
        X = ini()
        l = bisect_right(A, X)
        r = l
        ans = 0
        if l >= 0:
            ans += l*X - sums[l]
        if r < N:
            ans += sums[N] - sums[r] - (N-r)*X
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