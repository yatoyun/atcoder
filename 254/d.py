from collections import defaultdict
def main():
    N = ini()
    
    sq = [False]*(N+1)
    d = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        if i*i > N:
            break
        sq[i*i] = True
    
    for i in range(1, N+1):
        for j in range(i, N+1, i):
            d[j].append(i)
    cnt = [0]*(N+1)
    for i in range(1, N+1):
        f = 0
        for j in d[i]:
            if sq[j]:
                f = j
        if f == 0:
            cnt[i] += 1
            continue
        cnt[i//f] += 1
    ans = 0
    for i in range(1, N+1):
        ans += cnt[i]**2
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
