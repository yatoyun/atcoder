

def f(x, next_num) -> int:
    next_x = [x[0], next_num]
    diff = int(next_num) - int(x[0])
    num = int(next_num)
    for i in range(2, len(x)):
        num += diff
        if num > 9 or num < 0:
            return None
        next_x.append(num)
    return int("".join(map(str, next_x)))

def main():
    X = ini()
    str_x = list(map(int, str(X)))
    
    if len(str_x) == 1:
        print(X)
        return
    
    for i in range(str_x[0], 10):
        str_x[0] = i
        for j in range(1, 10):
            num = f(str_x, j)
            if num is None:
                continue
            if num >= X:
                print(num)
                return
    
    if len(str_x) < 10:
        num = int("".join(map(str, [range(1, len(str_x)+1)])))
        print(num)
        return
    
    if len(str_x) == 10 and X <= 9876543210:
        print(9876543210)
        return
    
    num = int("".join(map(str, [1]**(len(str_x)+1))))
    print()

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