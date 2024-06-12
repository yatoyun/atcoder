def main():
    N, X, Y = mapint()
    
    Rnums = [0]*(N+1)
    Bnums = [0]*(N+1)
    
    Rnums[N] = 1
    for i in range(N, 1, -1):
        red = Rnums[i]
        Rnums[i-1] += red
        Bnums[i] += X*red
        
        blue = Bnums[i]
        Rnums[i-1] += blue
        Bnums[i-1] += Y*blue
    
    print(Bnums[1])
            

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
