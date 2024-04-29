from collections import defaultdict

def main():
    N, T = input().split()
    N = int(N)
    T = list(T)
    
    S = [lstr() for _ in range(N)]
    
    left_index_dict = defaultdict(int)
    right_index_dict = defaultdict(int)
    
    for i in range(N):
        s = S[i]
        cntL = 0
        cntR = 0
        for j in range(len(s)):
            if cntL < len(T) and s[j] == T[cntL]:
                cntL += 1
            if cntR < len(T) and s[-1-j] == T[-1-cntR]:
                cntR += 1
        left_index_dict[cntL] += 1
        right_index_dict[cntR] += 1
    sumR = [0]*(len(T)+1)
    sumR[-1] = right_index_dict[len(T)]
    for i in range(len(T)-1, -1, -1 ):
        sumR[i] = sumR[i+1] + right_index_dict[i]
    
    ans = 0
    for v in left_index_dict:
        ans += left_index_dict[v]*sumR[len(T)-v]
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