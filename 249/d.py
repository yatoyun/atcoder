from collections import defaultdict
def main():
    N = ini()
    A = lint()
    
    nums = [0] * (max(A)+1)
    nums_dict = defaultdict(int)
    for a in A:
        nums[a] += 1
        nums_dict[a] += 1
    ans = 0
    for a, v in nums_dict.items():
        cnt = 0
        for x in range(1, int(a**0.5)+1):
            if a%x==0:
                if x == a//x:
                    cnt += nums[x] * nums[x]
                    continue
                cnt += nums[x] * nums[a//x] * 2
        ans += cnt * v
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