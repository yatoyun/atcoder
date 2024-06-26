from collections import defaultdict
def main():
    N, K = mapint()

    S_list = [lstr() for _ in range(N)]

    S_alpha_dict = []
    for i in range(N):
        S_alpha_dict.append(defaultdict(int))
        for j in range(len(S_list[i])):
            S_alpha_dict[i][S_list[i][j]] += 1

    ans = 0
    for bit in range(1<<N):
        alpha_dict = defaultdict(int)
        for i in range(N):
            if bit & (1<<i):
                for k, v in S_alpha_dict[i].items():
                    alpha_dict[k] += v
        cnt = 0
        for k, v in alpha_dict.items():
            if K == v:
                cnt += 1
        ans = max(ans, cnt)
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