from collections import defaultdict
def main():
    N = ini()
    S = [input().rstrip() for _ in range(N)]
    
    sortedIndex = sorted(range(N), key=lambda x: S[x])
    sortedS = sorted(S)
    
    ans = [0]*N
    for i in range(N):
        def check(com_i):
            if com_i < 0 or com_i >= len(sortedS):
                return 0
            cnt = 0
            for j in range(min(len(sortedS[com_i]), len(sortedS[i]))):
                if sortedS[com_i][j] == sortedS[i][j]:
                    cnt += 1
                else:
                    break
            return cnt
            
        cnt = max(check(i-1), check(i+1))
        ans[sortedIndex[i]] = cnt
    for a in ans:
        print(a)
        

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