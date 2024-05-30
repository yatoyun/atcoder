def main():
    X = lstr()
    
    nums = [0]*len(X)
    
    sums = [0]*len(X)
    sums[0] = int(X[0])
    for i in range(1, len(X)):
        sums[i] = sums[i-1] + int(X[i])
    
    for i in range(len(X)-1, -1, -1):
        nums[i] += sums[i]
        if nums[i] >= 10 and i > 0:
            nums[i-1] += nums[i]//10
            nums[i] %= 10
    
    front = ""
    if nums[0] >= 10:
        front = str(nums[0]//10)
        nums[0] %= 10
    print(front, end="")
    for n in nums:
        print(n, end="")


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
    sys.set_int_max_str_digits(500000)
    input = sys.stdin.readline
    atcenv = os.environ.get("ATCODER", 0)
    main()