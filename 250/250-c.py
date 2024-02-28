import sys
input = sys.stdin.readline


def main():
    N, Q = map(int, input().split())
    A = [x for x in range(0, N+1)]
    B = [x for x in range(0, N+1)]

    for _ in range(Q):

        i = int(input())
        if B[i] == N:
            j = A[B[i]-1]
            A[B[i]], A[B[i]-1] = A[B[i]-1], A[B[i]]
            B[i] = B[j]
            B[j] = B[i]
        else:
            j = A[B[i]+1]
            A[B[i]], A[B[i]+1] = A[B[i]+1], A[B[i]]
            B[j] = B[i]
            B[i] = B[i]+1
    for i in range(1, N+1):
        print(A[i], end=' ')


if __name__ == "__main__":
    main()
