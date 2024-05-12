from collections import defaultdict
def main():
    N = ini()
    S = list(input().rstrip().split())
    
    S.sort()
    common_cnts = [0]*N
    for i in range(N-1):
        cnt = 0
        for j in range(len(S[i])):
            if S[i][j]==S[i+1][j]:
                cnt += 1
            else:
                break
        common_cnts[i] = cnt
    cnts = [0]*N
    for i in range(N-1, 0, -1):
        if common_cnts[i-1]==0:
            cnts[i-1] = 0
            continue
        cnts[i-1] += 1
    
    ans = sum_of_min_subarrays(common_cnts)

    print(ans)

def sum_of_min_subarrays(A):
    # 初期化
    result = 0
    stack = []
    n = len(A)
    
    # 各要素についてスタックを使用して処理
    for i in range(n):
        # 現在の要素より大きい要素を持つインデックスをスタックから取り除く
        while stack and A[stack[-1]] > A[i]:
            mid = stack.pop()
            left = stack[-1] if stack else -1
            # 左側からmidまでの要素数 * midからiまでの要素数 * A[mid]
            result += A[mid] * (mid - left) * (i - mid)
        
        stack.append(i)
    
    # スタックに残った要素を処理
    while stack:
        mid = stack.pop()
        left = stack[-1] if stack else -1
        # 左側からmidまでの要素数 * midから最後までの要素数 * A[mid]
        result += A[mid] * (mid - left) * (n - mid)
    
    return result

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