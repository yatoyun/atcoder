from atcoder.modint import Modint, ModContext
def main():
    N, M = mapint()
    
    mod = 998244353
    
    with ModContext(mod):
        # 2人
        dp = Modint(M * (M-1))
        for i in range(2, N):
            dp = Modint(M)*(Modint(M-1)**i)-dp
        print(dp.val())
        

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