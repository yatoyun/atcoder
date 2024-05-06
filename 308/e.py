def main():
    N = ini()
    A = lint()
    S = lstr()
    
    Mnums = [[0]*3 for _ in range(N)]
    for i in range(N):
        for j in range(3):
            Mnums[i][j] = Mnums[i-1][j] if i>0 else 0
        if S[i]=="M":
            Mnums[i][A[i]] += 1
    
    Xnums = [[0]*3 for _ in range(N)]
    for i in range(N-1, -1, -1):
        for j in range(3):
            Xnums[i][j] = Xnums[i+1][j] if i<N-1 else 0
        if S[i]=="X":
            Xnums[i][A[i]] += 1
    
    errprint(Mnums)
    errprint(Xnums)
    ans = 0
    for i in range(1,N-1):
        x = A[i]
        num_set = [0]*3
        num_set[0] = x
        if S[i] == "E":
            Mnum = Mnums[i-1]
            Xnum = Xnums[i+1]
            for j in range(3):
                num_set[1] = j
                for k in range(3):
                    num_set[2] = k
                    min_num = 0
                    for l in range(4):
                        if l not in num_set:
                            min_num = l
                            break
                    ans += Mnum[j]*Xnum[k]*min_num
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