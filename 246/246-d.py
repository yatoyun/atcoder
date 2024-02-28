import sys

input = sys.stdin.readline

def calc(a, b):
    return (a**3 + a**2 * b + a * b**2 + b**3)

def main():
    x = int(input())
    a = 0
    b = 1000000
    ans = 10**100

    while a <= b:
        value = calc(a, b)
        if value >= x:
            ans = min(ans, value)
            b -= 1
        else:
            a += 1
    print(ans)

if __name__ == "__main__":
    main()