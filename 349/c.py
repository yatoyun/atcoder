def main():
    S = lstr()
    T = lstr()
    if T[-1] == "X":
        T.pop()
    i = 0
    j = 0
    while i < len(S):
        if S[i] == T[j].lower():
            j += 1
        i += 1
        if j == len(T):
            print("Yes")
            return
    print("No")

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