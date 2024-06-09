from collections import defaultdict
from itertools import permutations

def main():
    H1, W1 = mapint()
    A = [lint() for _ in range(H1)]

    H2, W2 = mapint()
    B = [lint() for _ in range(H2)]

    if H1 < H2 or W1 < W2:
        print("No")
        return

    a_rows = [defaultdict(int) for _ in range(H1)]
    a_cols = [defaultdict(int) for _ in range(W1)]
    for i in range(H1):
        for j in range(W1):
            a_rows[i][A[i][j]] += 1
            a_cols[j][A[i][j]] += 1
    
    b_rows = [defaultdict(int) for _ in range(H2)]
    b_cols = [defaultdict(int) for _ in range(W2)]
    for i in range(H2):
        for j in range(W2):
            b_rows[i][B[i][j]] += 1
            b_cols[j][B[i][j]] += 1
    
    def check_contain(a, b):
        if len(a) < len(b):
            return False
        for k, v in b.items():
            if a[k] < v:
                return False
        return True
    
    new_rows = []
    # rows
    index = 0
    for i in range(H2):
        while index < H1:
            if check_contain(a_rows[index], b_rows[i]):
                new_rows.append(A[index])
                index += 1
                break
            index += 1
    if len(new_rows) < H2:
        print("No")
        return
    
    cotain_indexs = []
    # cols
    index = 0
    for i in range(W2):
        while index < W1:
            if check_contain(a_cols[index], b_cols[i]):
                cotain_indexs.append(index)
                index += 1
                break
            index += 1
    if len(cotain_indexs) < W2:
        print("No")
        return
    
    for i in range(len(new_rows)):
        new_rows[i] = [new_rows[i][j] for j in range(W1) if j in cotain_indexs]
    A = new_rows
    for permH in permutations(range(len(A)), H2):
        for permW in permutations(range(len(A[0])), W2):
            for i in range(H2):
                for j in range(W2):
                    if A[permH[i]][permW[j]] != B[i][j]:
                        break
                else:
                    continue
                break
            else:
                print("Yes")
                return
    print("No")


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