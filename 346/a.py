import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ex = A[0]
    for a in A[1:]:
        print(ex * a, end=" ")
        ex = a

if __name__ == "__main__":
    main()