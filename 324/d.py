import sys
input = sys.stdin.readline

def main():
    N = int(input())
    S = input().strip()
    count_0 = S.count("0")
    if count_0 == N:
        print(1)
        return
    ans = 0
    for _ in range(count_0+1):
        c = [0]*10
        for i in S:
            c[int(i)] += 1
        
        max_num = int(pow(int("".join(sorted(S,reverse=True))),1/2))
        sort_S = sorted(S)
        for j in range(len(sort_S)):
            if sort_S[j] != "0":
                sort_S[0], sort_S[j] = sort_S[j], sort_S[0]
                break
        min_num = int(pow(int("".join(sort_S)),1/2))
        for j in range(min_num, max_num+1):
            str_ii = str(j*j)
            nc = [0]*10
            for i in str_ii:
                nc[int(i)] += 1
            if c == nc:
                ans += 1
        S = S.replace("0", "", 1)
    print(ans)
if __name__ == "__main__":
    main()
