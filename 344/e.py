def main():
    N = ini()
    A = lint()
    a_dict = {}
    a_dict_reverse = {}
    a_dict[0] = A[0]
    a_dict_reverse[A[0]] = 0
    for i in range(1, N):
        a_dict[A[i-1]] = A[i]
        a_dict_reverse[A[i]] = A[i-1]
    errprint(a_dict)
    errprint(a_dict_reverse)
    Q = ini()
    for i in range(Q):
        q, *order = mapint()
        if q == 1:
            x, y = order
            if x not in a_dict:
                a_dict[x] = y
                a_dict_reverse[y] = x
            else:
                ex_a = a_dict[x]
                a_dict[x] = y
                a_dict[y] = ex_a
                a_dict_reverse[ex_a] = y
                a_dict_reverse[y] = x
        elif q == 2:
            x = order[0]
            if x in a_dict:
                next_x = a_dict[x]
                ex_x = a_dict_reverse[x]
                del a_dict[x]
                del a_dict_reverse[x]
                a_dict[ex_x] = next_x
                a_dict_reverse[next_x] = ex_x
            else:
                ex_x = a_dict_reverse[x]
                del a_dict[ex_x]
                del a_dict_reverse[x]
            
        errprint(a_dict)
    crr = 0
    while True:
        if crr not in a_dict:
            break
        print(a_dict[crr], end=" ")
        crr = a_dict[crr]

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