from collections import defaultdict

def main():
    S = lstr()
    
    num_l = [0]*10
    comb = defaultdict(int)
    comb[tuple(num_l)] = 1
    for i in range(len(S)):
        num_l[int(S[i])] += 1
        num_l[int(S[i])] %= 2
        comb[tuple(num_l)] += 1
    
    ans = 0
    for v in comb.values():
        ans += v*(v-1)//2
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