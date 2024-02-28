import sys
input = sys.stdin.readline

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = int(input())
    
    for i in range(Q):
        a, b = map(int, input().split())
        index_a = P.index(a)
        index_b = P.index(b)
        if index_a < index_b:
            print(a)
        else:
            print(b)

if __name__ == "__main__":
    main()