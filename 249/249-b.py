import sys
input = sys.stdin.readline


def main():
    S = input()
    T = []

    for s in S:
        if not (s in T):
            T.append(s)
        else:
            print("No")
            return

    if S.islower() or S.isupper():
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
