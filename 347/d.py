def main():
    a, b, C = mapint()
    C = format(C, "b")
    
    reverse_flag = False
    if a < b:
        b, a = a, b
        reverse_flag = True
    diff = a - b
    a_flag = True
    X = [-1]*len(C)
    Y = [-1]*len(C)
    for i, s in enumerate(C[::-1]):
        if s == "0":
            continue
        if diff > 0:
            X[i] = 1
            Y[i] = 0
            a -= 1
            diff -= 1
        elif a_flag:
            X[i] = 1
            Y[i] = 0
            a -= 1
            a_flag = False
        else:
            X[i] = 0
            Y[i] = 1
            b -= 1
            a_flag = True
    if a != b or a < 0 or b < 0:
        print(-1)
        return
    for i in range(len(C)):
        if X[i] != -1:
            continue
        if a > 0:
            X[i] = 1
            Y[i] = 1
            a -= 1
        else:
            X[i] = 0
            Y[i] = 0
    while a:
        X.append(1)
        Y.append(1)
        a -= 1
    X = "".join(map(str, X[::-1]))
    Y = "".join(map(str, Y[::-1]))
    if reverse_flag:
        X, Y = Y, X
    if len(X) > 60 or len(Y) > 60:
        print(-1)
        return
    X, Y = int(X, 2), int(Y, 2)
    if X ^ Y == int(C, 2):
        print(X, Y)
    else:
        print(-1)
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