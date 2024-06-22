from math import lcm

def calc_sum(N, X):
    max_n_X = int(N//X)
    total_sum_A = (X*max_n_X*(max_n_X+1))//2
    return total_sum_A


def main():
    N, A, B = mapint()

    total_sum_1N = (N*(N+1))//2
    total_sum_A = calc_sum(N, A)
    total_sum_B = calc_sum(N, B)
    total_sum_AB = calc_sum(N, lcm(A, B))
    if A == B:
        ans = total_sum_1N - total_sum_A
        print(ans)
        return
    ans = total_sum_1N - total_sum_A - total_sum_B + total_sum_AB
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