from collections import deque
from atcoder.modint import Modint, ModContext
mod = 998244353
def main():
    Q = ini()
    S = 1
    with ModContext(mod):
        S = Modint(S)
        removal = deque([1])
        for _ in range(Q):
            query = lint()
            if query[0]==1:
                x = query[1]
                S = S*10 + x
                removal.append(x)
            elif query[0]==2:
                x = removal.popleft()
                S -= Modint(10)**(len(removal))*x
            else:
                print(S.val())

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
