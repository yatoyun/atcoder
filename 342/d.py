from collections import defaultdict

def main():
    N = ini()
    A = lint()
    max_a = max(A)
    square_nums = [0]*(max_a+1)
    square_nums[0] = 1
    for i in range(2, int(max_a**0.5)+1):
        for j in range(1, max_a//i**2+1):
            square_nums[i**2*j] = j
    errprint(square_nums)
    nums_dict = defaultdict(int)
    zeros = 0
    for i in range(N):
        if A[i] == 0:
            zeros += 1
            continue
        if square_nums[A[i]] == 0:
            nums_dict[A[i]] += 1
        else:
            nums_dict[square_nums[A[i]]] += 1
    errprint(nums_dict)
    cnt = 0
    for v in nums_dict.values():
        cnt += v*(v-1)//2
    cnt += zeros*(N-zeros)
    cnt += zeros*(zeros-1)//2
    print(cnt)
            

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