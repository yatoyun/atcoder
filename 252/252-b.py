import sys
import itertools
input = sys.stdin.readline


def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()

    T = []
    ans = set()
    count = 0

    for a in A:
        if a <= W:
            T.append(a)
            ans.add(a)
        else:
            break
    count += len(T)

    if N > 1:
        for a, b in itertools.combinations(T, 2):
            if a+b <= W:
                ans.add(a+b)

    if N > 2:
        for a, b, c in itertools.combinations(T, 3):
            if a+b+c <= W:
                ans.add(a+b+c)

    print(len(ans))


if __name__ == "__main__":
    main()
