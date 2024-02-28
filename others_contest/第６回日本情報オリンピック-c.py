import sys
input = sys.stdin.readline

def main():
    n = int(input())
    xy = [tuple(map(int, input().split())) for _4 in range(n)]
    set_xy = set(xy)

    ans = 0
    for i in range(n-1):
        x1, y1 = xy[i]
        for j in range(i+1, n):
            x2, y2 = xy[j]
            dx = x1 - x2
            dy = y1 - y2

            if (x1 + dy, y1 - dx) in set_xy and (x2 + dy, y2 - dx) in set_xy:
                ans = max(ans, dx ** 2 + dy ** 2)
    print(ans)
    return
        



if __name__ == "__main__":
    main()