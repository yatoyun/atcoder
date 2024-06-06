def cross_product(v1, v2):
    return v1[0]*v2[1] - v1[1]*v2[0]

def vec(v1, v2):
    return (v2[0]-v1[0], v2[1]-v1[1])

def main():
    XY = [lint() for _ in range(4)]
    
    XY.append(XY[0])
    XY.append(XY[1])
    
    ex_vec = vec(XY[0], XY[1])
    for i in range(1, 5):
        curr = vec(XY[i], XY[i+1])
        if cross_product(ex_vec, curr) <= 0:
            print("No")
            return
        ex_vec = curr
        
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