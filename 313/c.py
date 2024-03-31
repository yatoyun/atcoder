import heapq 

def main():
    N = ini()
    A = lint()
    
    if N == 1:
        print(0)
        return
    
    target = sum(A)//N
    r = sum(A)%N
    A.sort()
    B = sum([abs(target-a) if i < N-r else abs(target+1-a) for i, a in enumerate(A)])
    print(B//2)
            

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