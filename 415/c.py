from collections import deque

def main():
    T = ini()
    for _ in range(T):
        N = ini()
        S = lstr()
        if S[-1] == "1":
            print("No")
            continue

        full = (1 << N) - 1
        que = deque()
        que.append(0)
        visited = set()
        yes = False
        while que:
            st = que.popleft()
            if st == full:
                yes = True
                break
            if st > full:
                continue
            for i in range(N):
                if 1 << i & st:
                    continue
                new_st = st | (1 << i)
                if S[new_st-1] == "0" and new_st not in visited:
                    visited.add(new_st)
                    que.append(new_st)
        print("Yes" if yes else "No")


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