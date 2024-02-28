import sys
import itertools
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())

    A = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i, j in itertools.combinations(range(M), 2):
        sum = 0
        for a in A:
            if a[i] > a[j]:
               sum += a[i]
            else:
                sum += a[j]
        ans = max(ans, sum)
    print(ans)


if __name__ == "__main__":
    main()