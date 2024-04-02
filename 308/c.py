from functools import cmp_to_key
def check(a, b):
    def calc(x, y):
        return x[0] * (y[0]+y[1])
    if calc(a,b) > calc(b,a):
        return -1
    elif calc(a,b) < calc(b,a):
        return 1
    else:
        if a[2] > b[2]:
            return 1
        elif a[2] < b[2]:
            return -1
        

def main():
    N = ini()
    prob_list = []
    for i in range(N):
        a, b = mapint()
        prob_list.append((a, b, i+1))
    # sort by x[0] but if x[0] is same, sort by x[1]
    prob_list.sort(key=cmp_to_key(check))
    
    for _, _, i in prob_list:
        print(i, end=" ")
    

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