import sys
input = sys.stdin.readline

def main():
    N, T = input().split()
    N = int(N)
    
    ans = []
    for i in range(1, N+1):
        S = input().strip()
        if len(S) == len(T):
            flag = False
            for j in range(len(S)):
                if S[j] != T[j]:
                    if flag:
                        flag = None
                        break
                    flag = True
            if flag is not None:
                ans.append(i)
        elif len(S) == len(T) - 1:
            flag = False
            js, jt = 0, 0
            while js < len(S) and jt < len(T):
                if S[js] != T[jt]:
                    if flag:
                        flag = None
                        break
                    flag = True
                    jt += 1
                else:
                    js += 1
                    jt += 1
            if flag is not None:
                ans.append(i)
        elif len(S) == len(T) + 1:
            flag = False
            js, jt = 0, 0
            while js < len(S) and jt < len(T):
                if S[js] != T[jt]:
                    if flag:
                        flag = None
                        break
                    flag = True
                    js += 1
                else:
                    js += 1
                    jt += 1
            if flag is not None:
                ans.append(i)
    print(len(ans))
    print(*ans)

if __name__ == "__main__":
    main()
