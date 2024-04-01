

def main():
    N = ini()
    B = lint0()
    
    visited = set()
    for i in range(N):
        if i in visited:
            continue
        rabbit = i
        turtle = i
        ans = None
        while True:
            rabbit = B[rabbit]
            rabbit = B[rabbit]
            turtle = B[turtle]
            visited.add(turtle)
            if rabbit == turtle:
                ans = turtle
                break
        if ans is not None:
            turtle = ans
            count = 0
            while True:
                turtle = B[turtle]
                count += 1
                if turtle == ans:
                    break
            print(count)
            turtle = ans
            while True:
                turtle = B[turtle]
                print(turtle+1, end=" ")
                if turtle == ans:
                    return
    
    

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