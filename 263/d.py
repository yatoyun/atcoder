def main():
    N, L, R = mapint()
    A = lint()
    
    sums_l = [0]*N
    sums_l[0] = A[0]
    for i in range(1, N):
        sums_l[i] = sums_l[i-1] + A[i]
        
    sums_r = [0]*N
    sums_r[0] = A[-1]
    for i in range(1, N):
        sums_r[i] = sums_r[i-1] + A[N-i-1]
    sums_r = sums_r[::-1]
    
    max_diff_l = [0]*N
    for i in range(N):
        diff = sums_l[i] - L*(i+1)
        max_diff_l[i] = max(0, diff, max_diff_l[i-1])
    
    
    max_diff_r = [0]*N
    for i in range(1,N+1):
        diff = sums_r[-i] - R*(i)
        max_diff_r[-i] = max(0, diff, max_diff_r[-i+1])
    
    max_v = max_diff_r[0]
    for i in range(N-1):
        if max_diff_l[i] + max_diff_r[i+1] > max_v:
            max_v = max_diff_l[i] + max_diff_r[i+1]
    if max_diff_l[-1] > max_v:
        max_v = max_diff_l[-1]
    
    print(sum(A)- max_v)
    

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