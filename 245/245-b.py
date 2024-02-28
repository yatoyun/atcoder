import sys
input = sys.stdin.readline

def main():
    n = int(input())

    a = [int(x) for x in input().split()]
    a.sort()

    x = 0
    c = -1

    for b in a:
        if c == b:
            continue
        if x == b:
            c = b
            x += 1
        else:
            print(x)
            exit()
    print(x)

if __name__ == "__main__":
    main()