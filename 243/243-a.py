import sys
input = sys.stdin.readline


def main():
    V, A, B, C = map(int, input().split())

    if V >= A + B + C:
        V %= (A+B+C)
    if V >= A:
        V -= A
    else:
        print("F")
        exit()
    if V >= B:
        V -= B
    else:
        print("M")
        exit()
    if V >= C:
        V -= C
    else:
        print("T")
        exit()


if __name__ == '__main__':
    main()
