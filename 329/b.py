import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(set(map(int, input().split())))

    A.sort()
    print(A[-2])
    
if __name__ == "__main__":
    main()