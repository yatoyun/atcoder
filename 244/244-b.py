import sys
input = sys.stdin.readline

def main():
    n = int(input())
    inp = input()

    x = y = 0

    direction = 0

    for i in inp:
        if i == 'S':
            if direction == 0:
                x += 1
            elif direction == 1:
                y -= 1
            elif direction == 2:
                x -= 1
            elif direction == 3:
                y += 1
        elif i == 'R':
            if direction == 3:
                direction = 0
            else:
                direction += 1
    print(x, y)


if __name__ == "__main__":
    main()