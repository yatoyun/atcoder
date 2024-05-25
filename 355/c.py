def main():
    N, T = mapint()
    A = lint()
    
    rows = [0]*N
    cols = [0]*N
    slant1 = 0
    slant2 = 0
    
    for x in range(T):
        t = A[x]
        i = (t-1) // N
        j = (t-1) % N
        
        rows[i] += 1
        cols[j] += 1
        if i == j:
            slant1 += 1
        if i+j == N-1:
            slant2 += 1
        
        # check
        if rows[i] == N or cols[j] == N or slant1 == N or slant2 == N:
            print(x+1)
            return
    print(-1)
        

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