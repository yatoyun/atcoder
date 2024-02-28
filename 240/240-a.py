import sys
input = sys.stdin.readline

def main():
    a,b = map(int, input().split())
    if a+1 == b or a + 9 == b:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()