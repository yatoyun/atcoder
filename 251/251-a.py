import sys
input = sys.stdin.readline


def main():
    S = input().replace('\n', '')

    ans = ""

    for _ in range(int(6/len(S))):
        ans = ans + S
    print(ans)


if __name__ == '__main__':
    main()
