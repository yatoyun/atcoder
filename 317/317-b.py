import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    min_a = A[0]
    max_a = A[-1]
    sum_a = sum(A)
    
    act_sum = sum(range(min_a, max_a+1))
    
    print(act_sum-sum_a)

if __name__ == "__main__":
    main()