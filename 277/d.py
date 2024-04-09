def main():
    N, M = mapint()
    A = lint()
    
    A.sort()
    A_sum = sum(A)
    sum_l = [A[0]]
    for i in range(1, N):
        if A[i] == A[i-1] or A[i] == A[i-1]+1:
            sum_l[-1] += A[i]
        else:
            sum_l.append(A[i])
    end2st_sum = 0
    if A[0] == 0 and A[-1] == M-1 and len(sum_l) != 1:
        end2st_sum = sum_l[0] + (sum_l[-1])

    print(A_sum - max(max(sum_l), end2st_sum))
    

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