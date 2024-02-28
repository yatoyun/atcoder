import sys
input = sys.stdin.readline

def main():
    Q = int(input())
    
    ans = []
    for _ in range(Q):
        command, x = map(int, input().split())
        if command == 1:
            ans.append(x)
        else:
            print(ans[-1*x])

if __name__ == "__main__":
    main()
