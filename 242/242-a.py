import sys
input = sys.stdin.readline

def main():
    A, B, C, X = map(int, input().split())

    if X <= A:
        print(1/1)
    elif X <= B:
        print(C/(B-A))
    else:
        print(0/1)
    

if __name__ == "__main__":
    main()