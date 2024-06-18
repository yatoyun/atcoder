def main():
    X, A, D, N = mapint()
    
    if D == 0:
        print(abs(X-A))
        return
    
    def calc_abs(a, b):
        return abs(a-b)
    
    X -= A
    ans = abs(X)
    pred_cnt = abs(X // D)
    if abs(pred_cnt) >= N:
        print(min(calc_abs(X, (N-1)*D), ans))
        return
    left = calc_abs(X, (pred_cnt*D))
    right = calc_abs(X, (pred_cnt+1)*D)
    print(min([left, right, ans]))
    

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
