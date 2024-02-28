import sys
input = sys.stdin.readline

def main():
    n = input()
    A = list(map(int, input().split()))
    ans = []

    for a in A:
        if not (a in ans):
            ans.append(a)
    print(len(ans))

def tehon():
    n = int(input())
    print(len(set(map(int, input().split()))))

if __name__ == "__main__":
    main()
