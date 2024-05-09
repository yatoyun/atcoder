from bisect import bisect_left, bisect_right

def main():
    N, K = mapint()
    A = lint()
    ans = [0]
    
    for i in range(1, K+1):
        curr_max = ans[-1]
        next_max = float("inf")
        for a in A:
            index = bisect_right(ans, curr_max - a)
            if ans[index]+a < curr_max:
                continue
            next_max = min(next_max, ans[index]+a)
        ans.append(next_max)
    
    print(ans[-1])

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