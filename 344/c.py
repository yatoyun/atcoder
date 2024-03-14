import sys
input = sys.stdin.readline


def check(set_x, A, B, C):
    N = len(A)
    M = len(B)
    L = len(C)
    for i in range(N):
        for j in range(M):
            for k in range(L):
                sum_abc = A[i] + B[j] + C[k]
                set_x.add(sum_abc)
    return set_x

def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    L = int(input())
    C = list(map(int, input().split()))
    Q = int(input())
    X = list(map(int, input().split()))
    
    set_x = set()
    set_x = check(set_x, A, B, C)
    for x in X:
        if x in set_x:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()