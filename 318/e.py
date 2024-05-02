from collections import defaultdict

def main():
    N = ini()
    A = lint()
    
    numIndex = defaultdict(list)
    
    for i, a in enumerate(A):
        numIndex[a].append(i)
    
    ans = 0
    for i, v in numIndex.items():
        if len(v) == 1:
            continue
        
        for j in range(1, len(v)):
            ans += (v[j]-v[j-1]-1)*j*(len(v)-j)
            
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