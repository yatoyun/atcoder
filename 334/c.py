def main():
    N, K = mapint()
    A = lint()
    if K == 1:
        print(0)
        return
    
    A.sort()
    left = [0]
    for i in range(1, K, 2):
        left.append(left[-1] + (A[i] - A[i-1]))
    right = [0]
    for i in range(1, K, 2):
        right.append(right[-1] + (A[-i] - A[-i-1]))
    right = right[::-1]
    errprint(left)
    errprint(right)
    if K % 2 == 0:
        print(left[-1])
    else:
        ans = 10**18
        for i in range(len(left)):
            ans = min(ans, left[i] + right[i])
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
