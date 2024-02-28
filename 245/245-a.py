import sys
input = sys.stdin.readline

def main():
    output = ["Takahashi", "Aoki"]
    A, B, C, D = [int(x) for x in input().split()]

    if A > C:
        print(output[1])
    elif A == C:
        if B > D:
            print(output[1])
        else:
            print(output[0])
    else:
        print(output[0])

if __name__ == "__main__":
    main()