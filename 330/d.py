import sys
input = sys.stdin.readline

def count_Ls(cnt_o_rows, cnt_o_cols, i, j):
    cnt_row = cnt_o_rows[i] - 1
    cnt_col = cnt_o_cols[j] - 1
    return cnt_row * cnt_col

def main():
    N = int(input())
    S = []

    for _ in range(N):
        S.append(input().strip())
    
    cnt_o_rows = []
    for i in range(N):
        cnt = 0
        for j in range(N):
            if S[i][j] == "o":
                cnt += 1
        cnt_o_rows.append(cnt)
    
    cnt_o_cols = []
    for j in range(N):
        cnt = 0
        for i in range(N):
            if S[i][j] == "o":
                cnt += 1
        cnt_o_cols.append(cnt)
    
    cnt = 0
    for i in range(N):
        for j in range(N):
            if S[i][j] == "o":
                cnt += count_Ls(cnt_o_rows, cnt_o_cols, i, j)
    
    print(cnt)
if __name__ == "__main__":
    main()