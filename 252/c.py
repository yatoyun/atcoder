from collections import defaultdict, deque

def main():
    N = ini()
    S = [lstr() for _ in range(N)]
    indexes = defaultdict(list)

    for s in S:
        for i, x in enumerate(s):
            indexes[int(x)].append(i+1)
    ans = float("inf")
    for x in range(0, 10):
        indexes_x = indexes[x]
        indexes_x.sort()
        que = deque(indexes_x)
        time = 0
        start = 0
        while que:
            t = que.popleft()

            if start+1 <= t:
                start = t
            else:
                que.append(start+10)
        time += start
        ans = min(ans, time-1)
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