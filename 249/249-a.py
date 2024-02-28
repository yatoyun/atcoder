import sys
input = sys.stdin.readline


def calc_dis(A, B, C, X):
    a_distance = (X//(A+C))*A*B
    if X % (A+C) >= A:
        a_distance += A*B
    else:
        a_distance += B*(X % (A+C))
    return a_distance


def main():
    A, B, C, D, E, F, X = map(int, input().split())

    if calc_dis(A, B, C, X) > calc_dis(D, E, F, X):
        print("Takahashi")
    elif calc_dis(A, B, C, X) == calc_dis(D, E, F, X):
        print("Draw")
    else:
        print("Aoki")


if __name__ == "__main__":
    main()
