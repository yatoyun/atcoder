def main():
    N = ini()
    S = lstr()
    
    zero, one = 0, 0
    ans = 0
    for a in S:
        if a == '0':
            zero, one = 1, zero + one
        else:
            zero, one = one, zero + 1
        ans += one
        errprint(zero, one, ans)
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