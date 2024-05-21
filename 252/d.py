from collections import defaultdict
def main():
    N = ini()
    A = lint()
    
    nums = [0]*(max(A)+1)
    for a in A:
        nums[a] += 1
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    
    ans = 0
    for j in range(N):
        x = A[j]
        ans += nums[x-1]*(nums[-1]-nums[x])
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