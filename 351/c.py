from collections import deque

def main():
    N = ini()
    A = lint()
    
    if N == 1:
        print(1)
        return
    
    index = 0
    stack = []
    while index < N:
        stack.append(A[index])
        index += 1
        errprint(stack)
        while True:
            if len(stack) <= 1:
                break    
            if stack[-1] == stack[-2]:
                a = stack.pop()
                stack[-1] = a+1
            else:
                break
    print(len(stack))

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