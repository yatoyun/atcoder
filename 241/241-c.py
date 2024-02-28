import sys
input = sys.stdin.readline

N = int(input())
S = [input() for _ in range(N)]

def calc(x, y, dx, dy):
    count = 0

    for i in range(6):
        if not(0 <= min(x, y) and max(x, y) < N):
            return False
        if S[x][y] == '#':
            count += 1
        x += dx
        y += dy
    return count >= 4

def main():
    DX = [1, 0, 1, -1]
    DY = [0, 1, 1, 1]

    for i in range(N):
        for j in range(N):
            for dx, dy in zip(DX, DY):
                if calc(i, j, dx, dy):
                    print("Yes")
                    exit()
    print("No")

        
if __name__ == "__main__":
    main()
