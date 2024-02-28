import sys
input = sys.stdin.readline

def main():
    n, k, x = map(int,input().split())

    a = list(map(int,input().split()))

    a.sort(reverse=True)

    for i in range(n):
        if k == 0:
            break
        minus_k = min(k, a[i] // x)
        a[i] -= x * minus_k
        k -= minus_k

    if k != 0:
        a.sort(reverse=True)
        for i in range(n):
            if k == 0:
                break
            a[i] -= x
            k -= 1
            if a[i] < 0:
                a[i] = 0

    print(sum(a))

if __name__ == "__main__":
    main()