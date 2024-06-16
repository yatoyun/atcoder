from bisect import bisect_left, bisect_right
def main():
    N = ini()
    S = list(map(int, lstr()))

    W = lint()

    arr = []
    for i in range(N):
        arr.append((W[i], S[i]))
    
    arr.sort(key=lambda x: x[0])
    W.sort()

    sums_adult = [0]*N
    sums_adult[0] = arr[0][1]
    for i in range(1, N):
        sums_adult[i] = sums_adult[i-1] + arr[i][1]

    def calc_fx(idx):
        num_pred_children = idx+1
        num_pred_adult = N - num_pred_children
        correct = min(idx+1, idx+1-sums_adult[idx]) + min(num_pred_adult, (sums_adult[N-1] - sums_adult[idx]))
        return correct
    ans = sums_adult[-1]
    for i in range(1, N):
        idx = bisect_left(W, arr[i][0])
        ans = max(ans, calc_fx(idx-1))
    ans = max(ans, calc_fx(N-1))
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