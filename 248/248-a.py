import sys
input = sys.stdin.readline

def main():
    S = input()

    S = [int(x) for x in S[:-1]]
    S.sort()

    for i in range(0, 9):
        if i != S[i]:
            print(i)
            exit()
    print(9)

if __name__ == "__main__":
    main()