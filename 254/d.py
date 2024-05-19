from collections import defaultdict
def main():
    N = ini()
    
    nums = [0 for _ in range(N+1)]
    num_num = defaultdict(int)
    for i in range(1, N+1):
        max_div = 1
        for j in range(int(i**0.5)+1, 1, -1):
            div = j * j
            if i%div == 0:
                max_div = div
                break
        nums[i] = i // max_div
        num_num[i // max_div] += 1

    ans = N
    for k, v in num_num.items():
        ans += (v-1)*v
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
