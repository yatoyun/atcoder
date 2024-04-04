def main():
    L, N1, N2 = mapint()
    vl1 = []
    vl2 = []
    for _ in range(N1):
        v, l = mapint()
        vl1.append((v, l + (vl1[-1][1] if vl1 else 0)))
    for _ in range(N2):
        v, l = mapint()
        vl2.append((v, l + (vl2[-1][1] if vl2 else 0)))
    
    cnt = 0
    i1 = 0
    i2 = 0
    crr = 0
    while i1<N1 and i2<N2:
        if vl1[i1][0] == vl2[i2][0]:
            cnt += min(vl1[i1][1], vl2[i2][1]) - crr
        crr = min(vl1[i1][1], vl2[i2][1])
        if vl1[i1][1] < vl2[i2][1]:
            i1 += 1
        else:
            i2 += 1
    print(cnt)


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
