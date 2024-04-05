from collections import defaultdict

def main():
    H, W = mapint()
    A = [lint() for _ in range(H)]
    
    cnt = 0
    for bit in range(1<<(H+W-2)):
        num_set = set([A[0][0]])
        crr = (0,0)
        errprint("bit:", format(bit, 'b'))
        for i in range(H+W-2):
            if bit & (1<<i):
                nx = (crr[0]+1, crr[1])
            else:
                nx = (crr[0], crr[1]+1)
            errprint("nx:", nx)
            if nx[0]>=H or nx[1]>=W:
                break
            v_nx = A[nx[0]][nx[1]]
            if v_nx in num_set:
                break
            num_set.add(v_nx)
            crr = nx
        if len(num_set)==(H+W-1) and crr == (H-1, W-1):
            cnt += 1
        errprint(num_set)
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
