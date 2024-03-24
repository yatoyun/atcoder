import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    A_set = set([a for a in A if a <= K])
    unseen_sum = K * (K + 1) // 2 - sum(A_set)
    print(unseen_sum)

if __name__ == "__main__":
    main()
