import sys
input = sys.stdin.readline

def main():
    a = list(map(int, input().split()))
    n = 0

    for _ in range(2):
        n = a[n]
    print(a[n])

if __name__ == "__main__":
    main()