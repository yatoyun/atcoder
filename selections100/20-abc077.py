import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    A.sort()
    B.sort()
    C.sort()
    
    ans = 0
    for b in B:
        a = bisect_left(A, b)
        c = bisect_right(C, b)
        ans += a * (len(C) - c)
    
    print(ans)


if __name__ == "__main__":
    main()