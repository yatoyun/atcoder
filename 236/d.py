

ans = 0
def recursion(nums, N, A, cnt):
    global ans
    if not any(nums):
        ans = max(ans, cnt)
        return
    for j in range(2*N):
        if nums[j]:
            i = j
            break
    nums[i] = False
    for j in range(i+1, 2*N):
        if not nums[j]:
            continue
        nums[j] = False
        recursion(nums, N, A, cnt ^ A[i][j-i-1])
        nums[j] = True
    nums[i] = True
    return

def main():
    N = ini()

    A = []
    for i in range(2*N-1):
        A.append(lint())
    
    recursion([True]*(2*N), N, A, 0)
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