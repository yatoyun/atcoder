from itertools import permutations

def main():
    N, M = mapint()
    
    S_list = [lstr() for _ in range(N)]
    
    for perm in permutations(range(N)):
        ex = perm[0]
        flag = True
        errprint(perm)
        for i in perm[1:]:
            cnt = 0
            for j in range(M):
                if cnt > 1:
                    break
                if S_list[ex][j] != S_list[i][j]:
                    cnt += 1
            if cnt != 1:
                flag = False
                break
            ex = i
        if flag:
            print("Yes")
            return
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