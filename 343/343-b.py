import sys
input = sys.stdin.readline

def main():
    N = int(input())
    graph = []
    for _ in range(N):
        side = list(map(int, input().split()))
        ans = []
        for i,s in enumerate(side):
            if s == 1:
                ans.append(i+1)
        print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()
