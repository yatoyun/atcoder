import sys
input = sys.stdin.readline

def main():
    N, X = map(int, input().split())

    A = list(map(int, input().split()))

    print(A.index(X)+1)

if __name__ == "__main__":
    main()