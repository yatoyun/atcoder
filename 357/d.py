from atcoder.modint import Modint, ModContext

def main():
    mod = 998244353

    N = ini()
    K = len(str(N))
    with ModContext(mod):
        ans = Modint(N)*(Modint(10)**(N*K)-1)// (Modint(10)**K-1)
        print(ans.val())

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