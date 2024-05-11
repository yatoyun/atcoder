def concat(a, b):
    return (a[0] + b[0], a[1] + b[1])

def warshall_floyd(d, n):
    for k in range(n):# 中継点
        for i in range(n):# 始点
            for j in range(n):# 終点
                # 繰り返し見ていくので、現時点の i から j へ向かうコスト と 今検証している k を経由して j に向かうコスト の小さい方を i から j へ向かうコストとして登録する
                if d[i][j][0] > d[i][k][0] + d[k][j][0]:
                    d[i][j] = concat(d[i][k], d[k][j])
                elif d[i][j][0] == d[i][k][0] + d[k][j][0] and d[i][j][1] < d[i][k][1] + d[k][j][1]:
                    d[i][j] = concat(d[i][k], d[k][j])
    return d

def main():
    N = ini()
    A = lint()
    S = [lstr() for _ in range(N)]
    
    # warshall_floyd
    inf = 10**18
    dist = [[(inf, 0) for _ in range(N)] for _ in range(N)]
    # init
    for i in range(N):
        dist[i][i] = (0, 0)
        for j in range(N):
            if S[i][j] == 'Y':
                dist[i][j] = (1, A[j])
    # warshall_floyd
    dist = warshall_floyd(dist, N)
    Q = ini()
    for _ in range(Q):
        x, y = mapint0()
        if dist[x][y][0] == inf:
            print("Impossible")
        else:
            ans = dist[x][y]
            print(ans[0], ans[1]+A[x])


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