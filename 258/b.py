
def get_next_node(N, curr, dy, dx):
    y, x = curr

    if y + dy < 0:
        y = N - 1
    elif y + dy >= N:
        y = 0
    else:
        y += dy
    
    if x + dx < 0:
        x = N - 1
    elif x + dx >= N:
        x = 0
    else:
        x += dx
    
    return (y, x)

def main():
    N = ini()
    A = [lstr() for _ in range(N)]

    max_num = 0
    max_idyes = []
    for i in range(N):
        for j in range(N):
            if int(A[i][j]) > max_num:
                max_num = int(A[i][j])
                max_idyes = [(i, j)]
            elif int(A[i][j]) == max_num:
                max_idyes.append((i, j))
    ans = 0
    while max_idyes:
        st = max_idyes.pop()
        for dy, dx in [(0, 1),(-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]:
            num = A[st[0]][st[1]]
            curr = st
            for _ in range(N-1):
                nx, ny = get_next_node(N, curr, dy, dx)
                num += A[nx][ny]
                curr = (nx, ny)
            ans = max(ans, int(num))
    
    print(ans)


def ini(): return int(input())
def mapint(): return map(int, input().split())
def mapint0(): return map(lambda y: int(y)-1, input().split())
def mapstr(): return input().split()
def lint(): return list(map(int, input().split()))
def lint0(): return list(map(lambda y: int(y)-1, input().split()))
def lstr(): return list(input().rstrip())
def errprint(*y): return None if atcenv else print(*y, file=sys.stderr) 

if __name__=="__main__":
    import sys, os
    input = sys.stdin.readline
    atcenv = os.environ.get("ATCODER", 0)
    main()