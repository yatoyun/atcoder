def main():
    S = lstr()
    cnt = 0
    idxes = []
    for i, c in enumerate(S):
        if c == "#":
            cnt += 1
            idxes.append(i)
            if cnt % 2 == 0 and cnt > 0:
                print(f"{idxes[-2]+1},{idxes[-1]+1}")


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