from collections import deque

def main():
    atcoder = list("atcoder")
    S = lstr()

    S_set = set()
    que = deque([(S, 0)])
    while True:
        s, cnt = que.popleft()
        if s == atcoder:
            print(cnt)
            return

        if "".join(s) in S_set:
            continue
        S_set.add("".join(s))
        for i in range(len(s)-1):
            t = s.copy()
            t[i], t[i+1] = t[i+1], t[i]
            if "".join(t) not in S_set:
                que.append((t, cnt+1))

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