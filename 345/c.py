from collections import defaultdict
def main():
    S = lstr()
    lenS = len(S)
    dictS = defaultdict(int)
    ans = 0
    for s in S:
        dictS[s] += 1
    for i in range(lenS):
        cnt = lenS - dictS[S[i]]
        ans += cnt
    ans //= 2
    if max(dictS.values()) > 1:
        ans += 1
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