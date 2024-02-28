import sys
from collections import deque
q = deque()
input = sys.stdin.readline

def main():
    n, x = map(int, input().split())
    S = input()

    T = deque()

    for s in S:
        if s == 'U' and len(T) > 0 and (T[-1] == 'R' or T[-1] == 'L'):
            T.pop()
        else:
            T.append(s)

    for s in T:
        if s == 'U':
            x = int(x/2)
        elif s == 'L':
            x *= 2
        elif s == 'R':
            x = x*2 + 1
    print(x)
            

if __name__ == "__main__":
    main()