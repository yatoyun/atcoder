import sys
input = sys.stdin.readline

def calc_num_loop(Q, A):
    min_divide = 10**9
    
    for i in range(len(A)):
        if A[i] != 0 and Q[i] // A[i] < min_divide:
            min_divide = Q[i] // A[i]
    
    return min_divide

def main():
    N = int(input())
    Q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    max_amount = 0
    num_loop = calc_num_loop(Q, A)
    for i in range(num_loop+1):
        min_divide = 10**9
        for j in range(N):
            if B[j] != 0 and (Q[j] - i*A[j]) // B[j] < min_divide:
                min_divide = (Q[j] - i*A[j]) // B[j]
        amount = i + min_divide
        if amount > max_amount:
            max_amount = amount
    
    print(max_amount)

if __name__ == "__main__":
    main()