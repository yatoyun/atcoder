from collections import defaultdict, deque

def main():
    N = ini()
    S = [lstr() for _ in range(N)]
    
    P = []
    for i in range(N):
        for j in range(N):
            if S[i][j]=="P":
                P.append((i, j))
    scores = [[[[float("inf") for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    ans = float("inf")
    
    que = deque()
    que.append((0, P))
    while que:
        score, pos = que.popleft()
        p1, p2 = pos
        if scores[p1[0]][p1[1]][p2[0]][p2[1]] <= score:
            continue
        scores[p1[0]][p1[1]][p2[0]][p2[1]] = score
        if p1 == p2:
            ans = min(ans, score)
            continue
        if score >= ans:
            continue
        
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            def get_new_pos(pos, d):
                return (pos[0]+d[0], pos[1]+d[1])
            def valid_pos(pos):
                return 0<=pos[0]<N and 0<=pos[1]<N and S[pos[0]][pos[1]]!="#"
            npos1 = get_new_pos(p1, d)
            npos2 = get_new_pos(p2, d)
            valid_np1 = valid_pos(npos1)
            valid_np2 = valid_pos(npos2)
            if not valid_np1 and not valid_np2:
                continue
            if not valid_np1:
                npos1 = p1
            if not valid_np2:
                npos2 = p2
            que.append((score+1, (npos1, npos2)))
    print(ans if ans!=float("inf") else -1)

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