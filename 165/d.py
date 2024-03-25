import sys
input = sys.stdin.readline

def main():
    A, B, N = map(int, input().split())
    
    x = min(B-1, N)
    print(int(A*(x/B-x//B)))

if __name__ == "__main__":
    main()
