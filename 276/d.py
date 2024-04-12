def calc_divide(a, e):
    cnt = 0
    while a % e == 0:
        a //= e
        cnt += 1
    return cnt

def main():
    N = ini()
    A = lint()
    divide2_list = []
    divide3_list = []
    min_2 = float("inf")
    min_3 = float("inf")
    
    for i in range(N):
        a = A[i]
        num_divide_2 = calc_divide(a, 2)
        num_divide_3 = calc_divide(a, 3)
        
        divide2_list.append(num_divide_2)
        divide3_list.append(num_divide_3)
        min_2 = min(min_2, num_divide_2)
        min_3 = min(min_3, num_divide_3)
    
    errprint(divide2_list, divide3_list)
    ans = divide2_list[0]-min_2+divide3_list[0]-min_3
    
    def get_divide2(i):
        return pow(2, divide2_list[i]-min_2)
    def get_divide3(i):
        return pow(3, divide3_list[i]-min_3)
    def error():
        print(-1)
        exit(0)
    
    divide2 = get_divide2(0)
    divide3 = get_divide3(0)
    if A[0] % (divide2*divide3) != 0:
        error()
    A[0] = A[0]//(divide2*divide3)
    for i in range(1, N):
        divide2 = get_divide2(i)
        divide3 = get_divide3(i)
        errprint(divide2,divide3)
        if A[i] % (divide2*divide3) != 0:
            error()
        A[i] = A[i]//(divide2*divide3)
        errprint(A[i])
        if A[i] != A[i-1]:
            error()
        ans += divide2_list[i]-min_2+divide3_list[i]-min_3
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