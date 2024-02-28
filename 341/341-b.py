import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    for i in range(N-1):
        s, t = map(int, input().split())
        num = A[i] // s
        A[i] -= num * s
        A[i+1] += num * t
    print(A[-1])

if __name__ == "__main__":
    main()