from collections import deque
def main():
    N, K = mapint()
    A = lint()
    que = deque(A)
    
    curr = K
    cnt = 0
    while que:
        front = que.popleft()
        if front <= curr:
            curr -= front
        else:
            cnt += 1
            curr = K - front
    cnt += 1
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