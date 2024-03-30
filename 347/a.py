import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    for a in A:
        if a % K == 0:
            print(a//K, end=" ")

if __name__ == "__main__":
    main()