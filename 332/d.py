from itertools import permutations
def get_tuple_list(X, H, W):
    rows = [[] for _ in range(H)]
    cols = [[] for _ in range(W)]
    for i in range(H):
        for j in range(W):
            rows[i].append(X[i][j])
            cols[j].append(X[i][j])
    for i in range(H):
        rows[i] = tuple(sorted(rows[i]))
    for i in range(W):
        cols[i] = tuple(sorted(cols[i]))
    return rows, cols

def get_min_cnt(arr, diff_index, cnt):
    max_diff = [0,0]
    for i in range(len(arr)):
        index = diff_index[arr[i]]
        if index != i and abs(index - i) > max_diff[1] - max_diff[0]:
            max_diff = sorted([i, index])
    st = max_diff[0]
    ed = max_diff[1]
    if st == ed:
        return cnt
    # if st + 1 == ed and :
    for i in range(st, ed):
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
        cnt += 1
        
    # errprint(cnt ,arr)
    return get_min_cnt(arr, diff_index, cnt)

def main():
    H, W = mapint()
    A = [lint() for _ in range(H)]
    B = [lint() for _ in range(H)]
    
    ans = float("inf")
    for row_perms in permutations(range(H)):
        for col_perms in permutations(range(W)):
            # check
            for i in range(H):
                for j in range(W):
                    if A[row_perms[i]][col_perms[j]] != B[i][j]:
                        break
                else:
                    continue
                break
            else:
                errprint(row_perms, col_perms)
                row_inv = 0
                col_inv = 0
                for i in range(H):
                    for j in range(H):
                        if i < j and row_perms[i] > row_perms[j]:
                            row_inv += 1
                for i in range(W):
                    for j in range(W):
                        if i < j and col_perms[i] > col_perms[j]:
                            col_inv += 1
                ans = min(ans, row_inv+col_inv)
    if ans == float("inf"):
        print(-1)
    else:
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