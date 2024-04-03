def main():
    N = ini()
    S = lstr()
    is_not_use = dict()
    
    stack = []
    for i in range(N):
        if S[i]=="(":
            stack.append(i)
        elif S[i] == ")":
            if stack:
                st = stack.pop()
                is_not_use[st] = i
    st = 0
    ans = []
    while st < N:
        if st in is_not_use:
            st = is_not_use[st]
        else:
            ans.append(S[st])
        st += 1
    print("".join(ans))

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