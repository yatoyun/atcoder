import sys
from collections import defaultdict
from bisect import bisect_left
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    sorted_A = sorted(A)
    sum_dict = defaultdict(int)
    sum_dict[sorted_A[-1]] = 0

    ex = sorted_A[-1]
    for i, a in enumerate(sorted_A[::-1]):
        if a != ex:
            sum_dict[a] += sum_dict[sorted_A[-i]]
        next_index = bisect_left(sorted_A, a)-1
        if next_index >= 0:
            sum_dict[sorted_A[next_index]] += a
        ex = a

    for a in A:
        print(sum_dict[a], end=" ")
if __name__ == "__main__":
    main()