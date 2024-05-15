def main():
    N = ini()
    
    rowl = 1
    coll = 1
    rowr = N
    colr = N
    
    
    while rowr - rowl > 0:
        mid = (rowl+rowr)//2
        print(f"? {rowl} {mid} {coll} {colr}")
        flush()
        res = ini()
        if (mid-rowl+1) > res:
            rowr = mid
        else:
            rowl = mid+1
    ans_row = rowr
    rowl = 1
    rowr = N
    while colr - coll > 0:
        mid = (coll+colr)//2
        print(f"? {rowl} {rowr} {coll} {mid}")
        flush()
        res = ini()
        if (mid - coll +1) > res:
            colr = mid
        else:
            coll = mid+1
    ans_col = colr
    print(f"! {ans_row} {ans_col}")
    flush()

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
    flush = sys.stdout.flush
    input = sys.stdin.readline
    atcenv = os.environ.get("ATCODER", 0)
    main()