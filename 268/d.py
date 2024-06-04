from collections import defaultdict
def main():
    N = ini()
    P = lint()
    
    nums = defaultdict(int)
    for i in range(N):
        diff = P[i] - i
        if diff < 0:
            diff += N
        nums[diff] += 1
    
    errprint(nums)
    ans = 0
    for i in range(N):
        if i - 1 == -1:
            left = nums[9]
        else:
            left = nums[i - 1]
        mid = nums[i]
        if i + 1 == N:
            right = nums[0]
        else:
            right = nums[i + 1]
        errprint(left, mid, right)
        ans = max(ans, left + mid + right)
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