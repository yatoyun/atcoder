import sys
input = sys.stdin.readline


def main():
    A, M, L, R = map(int, input().split())
    
    L -= A
    R -= A
    
    print(R//M - (L-1)//M)
        

if __name__ == "__main__":
    main()