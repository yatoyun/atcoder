import sys
input = sys.stdin.readline


def main():
    N, A, B = map(int, input().split())

    ANS = [["."]*(101) for _ in range(101)]

    for i in range(N):
        for j in range(N):
            if i % 2 ^ j % 2:
                for m in range(A):
                    for n in range(B):
                        ANS[i*A+m][j*B+n] = "#"

    for i in range(A*N):
        for j in range(B*N):
            if j != B*N-1:
                print(ANS[i][j], end='')
            else:
                print(ANS[i][j])


if __name__ == "__main__":
    main()
