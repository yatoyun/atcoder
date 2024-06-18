def main():
    N = ini()
    LR = [lint() for _ in range(N)]
    LR.sort(key=lambda x: x[0])
    
    ans = []
    ex = LR[0]
    for i in range(1, N):
        if ex[1] < LR[i][0]:
            ans.append(ex)
            ex = LR[i]
        else:
            ex[1] = max(ex[1], LR[i][1])
    ans.append(ex)
    for a in ans:
        print(*a)

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
