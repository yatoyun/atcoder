def main():
    N = ini()
    A = lint()
    
    left = [0]*N
    right = [0]*N
    left[0] = 1
    right[0] = 1
    for i in range(1, N):
        if A[i] > left[i-1]:
            left[i] = left[i-1]+1
        elif A[i] == left[i-1]:
            left[i] = left[i-1]
        else:
            left[i] = A[i]
        
        if A[-i-1] > right[i-1]:
            right[i] = right[i-1]+1
        elif A[-i-1] == right[i-1]:
            right[i] = right[i-1]
        else:
            right[i] = A[-i-1]
    # errprint(left, right)
    ans = 0
    for i in range(N):
        ans = max(ans, min(left[i], right[N-i-1]))
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
