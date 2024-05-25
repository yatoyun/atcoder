def main():
    n, m = mapint()
    A = lint()
    B = lint()
    A_set = set(A)
    new_arr = A
    new_arr.extend(B)
    new_arr.sort()  
    
    flag = False
    for i in range(n+m):
        if flag:
            if new_arr[i] in A_set:
                print("Yes")
                return
            flag = False
        else:
            if new_arr[i] in A_set:
                flag = True
    print("No")

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