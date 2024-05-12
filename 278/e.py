from collections import defaultdict
def main():
    H, W, N, h, w = mapint()
    A = [lint0() for _ in range(H)]
    
    count = [[[0]*N for _ in range(W+1)] for _ in range(H+1)]
    
    for i in range(H):
        for j in range(W):
            for x in range(N):  # N は取りうる要素の種類の数
                if A[i][j] == x:
                    count[i][j][x] = 1
    
    # 列に関する累積和
    for x in range(N):
        for k in range(H):
            for l in range(W-2, -1, -1):
                count[k][l][x] += count[k][l+1][x]

    # 行に関する累積和
    for x in range(N):
        for k in range(H-2, -1, -1):
            for l in range(W):
                count[k][l][x] += count[k+1][l][x]
    
    for i in range(H-h+1):
        for j in range(W-w+1):
            cnt = 0
            for x in range(N):
                if count[0][0][x] - count[i][j][x] + count[i+h][j][x] + count[i][j+w][x] - count[i+h][j+w][x] > 0:
                    cnt += 1
            print(cnt, end=" ")
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