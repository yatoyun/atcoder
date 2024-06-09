from atcoder.modint import Modint, ModContext

def main():
    mod = 998244353

    N = ini()
    length = len(str(N))
    total = 0
    with ModContext(mod):
        final_ans = Modint(0)
        def calc(n, curr):
            return (Modint(10)**(length*n)) * curr
        while total < N:
            n = 1
            ans = (Modint(10)**(length*total))*Modint(N)
            while n + total <= N:
                if n + total + 1 != N and n * 2 + total <= N:
                    tmp = ans
                    ans += calc(n, tmp)
                    n *= 2
                else:
                    break
            total += n
            final_ans += ans
        print(final_ans.val())

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