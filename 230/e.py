def main():
    N = ini()
    
    stack = set()
    for i in range(1, int(N**0.5+1)):
        if N//i not in stack:
            stack.add(i)
            stack.add(N//i)
    
    stack = sorted(list(stack))
    ans = 0
    right = N
    while stack:
        left = stack.pop()
        num = N//right
        ans += num*(right-left)
        right = left
        
    ans += N
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