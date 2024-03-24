import sys
input = sys.stdin.readline

def main():
    B = int(input())
    
    for i in range(1, 18):
        A_A = pow(i, i)
        if A_A > B:
            print(-1)
            return
        elif A_A == B:
            print(i)
            return

if __name__ == "__main__":
    main()