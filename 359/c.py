def main():
    Sx, Sy = mapint()
    Tx, Ty = mapint()

    ans = abs(Ty-Sy)

    if Sx==Tx:
        print(ans)
        return
    if Sx > Tx:
        tx, sx = Sx, Tx
        flag = ((Tx+Ty) % 2 == 0)
    else:
        tx, sx = Tx, Sx
        flag = ((Sx+Sy) % 2 == 0)
    
    end_y = abs(Ty-Sy)
    y = 0
    if flag:
        sx += 1
    if sx+1==tx:
        print(ans)
        return
    if tx == sx:
        print(ans)
        return
    if end_y - y >= (tx-sx):
        errprint("b")
        print(ans)
        return
    
    sx += (end_y-y)
    ans += (tx-sx+1)//2
    print(ans)






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