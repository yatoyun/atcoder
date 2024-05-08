from atcoder.modint import Modint, ModContext

def main():
    mod = 998244353
    
    N, X = mapint()
    T = lint()
    
    with ModContext(mod):
        P = [Modint(0) for _ in range(X+1)] 
        r = Modint(1) // Modint(N)
        P[0] = Modint(1)
        ans = Modint(0)
        if T[0] > X:
            ans += P[0]
        
        for i in range(1,X+1):
            for t in T:
                if i - t >= 0:
                    P[i] += P[i-t]*r
            if i+T[0] > X:
                ans += P[i]
        ans *= r
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
