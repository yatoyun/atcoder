import sys
input = sys.stdin.readline

def main():
    N = int(input())
    
    ans = 0
    while N % 2**(ans+1) == 0:
        ans += 1
    print(ans)

if __name__ == "__main__":
    main()