def main():
    N, x, y = mapint()
    A = lint()
    row = []
    col = []
    for i in range(N):
        if i % 2 == 0:
            row.append(A[i])
        else:
            col.append(A[i])
    
    # row
    dp = set([row[0]])
    for i in range(1,len(row)):
        nxtdp = set()
        for j in dp:
            nxtdp.add(j+row[i])
            nxtdp.add(j-row[i])
        dp = nxtdp
        errprint(dp)
    if x not in dp:
        print("No")
        return
    # col
    dp = set([0])
    for i in range(len(col)):
        nxtdp = set()
        for j in dp:
            nxtdp.add(j+col[i])
            nxtdp.add(j-col[i])
        dp = nxtdp
        errprint(dp)
    if y not in dp:
        print("No")
        return
    print("Yes")

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