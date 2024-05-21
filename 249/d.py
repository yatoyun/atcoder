from collections import defaultdict
def main():
    N = ini()
    A = lint()
    max_a = max(A)
    nums = [0] * (max_a+1)
    nums_dict = defaultdict(int)
    for a in A:
        nums[a] += 1
        nums_dict[a] += 1
    ans = 0
    for q, q_v in nums_dict.items():
        cnt = 0
        for r in range(1,max_a+1):
            if q*r > max_a:
                break
            cnt += q_v * nums[r] * nums[q*r] # q*r = p
        ans += cnt
            
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