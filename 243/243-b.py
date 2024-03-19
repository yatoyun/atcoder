import sys
from collections import deque
input = sys.stdin.readline


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    count = 0
    count_i = 0
    for a, b in zip(A, B):
        if a == b:
            count_i += 1
    print(count_i)

    A.sort()
    B.sort()

    A = deque(A)
    B = deque(B)

    while len(A) > 0 and len(B) > 0:
        a = A.popleft()
        b = B.popleft()
        if a == b:
            count += 1
        elif a < b:
            B.appendleft(b)
        elif a > b:
            A.appendleft(a)
    print(count-count_i)


if __name__ == "__main__":
    main()
