import sys
input = sys.stdin.readline

def main():
    N = int(input())
    ans = ""
    for i in range(N):
        ans += "10"
    ans += "1"
    print(ans)

if __name__ == "__main__":
    main()