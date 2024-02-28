def main():
    n = int(input())
    numbers = [x for x in range(1, 2 * n + 2)]

    for _ in range(n+1):
        print(str(numbers.pop(0)))
        x = int(input())
        if x == 0:
            exit()
        numbers.remove(x)


if __name__ == "__main__":
    main()