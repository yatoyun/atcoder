import sys
input = sys.stdin.readline

def main():
    a = set(range(0,10))
    n,m = map(int, input().split())
    n += m
    a.remove(n)
    print(list(a)[0])

if __name__ == "__main__":
    main()
