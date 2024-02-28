import sys
from numpy import poly1d

input = sys.stdin.readline

def main():
    N, M = [int(x) for x in input().split()]

    A = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]

    polyA = poly1d(list(reversed(A)))
    polyC = poly1d(list(reversed(C)))

    polyB = polyC/polyA
    coefB = list(map(int, polyB[0].c))

    ans = list(reversed(coefB))
    print(*ans)

if __name__ == "__main__":
    main()