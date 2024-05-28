from collections import deque

def main():
    a, N = mapint()
    
    que = deque()
    que.append((1, 0))
    visited = set()
    while que:
        x, cost = que.popleft()
        if x == N:
            print(cost)
            return
        if x in visited:
            continue
        visited.add(x)
        if len(str(x)) > len(str(N)):
            continue
        
        que.append((x*a, cost+1))
        if x >= 10 and x%10 != 0:
            right_x = x % 10
            x = x // 10
            x = x + right_x * 10**(len(str(x)))
            que.append((x, cost+1))
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