from collections import defaultdict
def main():
    N = ini()
    
    ab_list = defaultdict(int)
    for i in range(1, N):
        for j in range(i, N, i):
            ab_list[j] += 1
    ans = 0
    for i in range(1, N+1):
        ab = ab_list[i]
        cd = ab_list[N-i]
        ans += ab * cd
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
