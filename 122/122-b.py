import sys
input = sys.stdin.readline

def main():
    S = input()

    S = [1 if x == 'A' or x == 'C' or x == 'G' or x == 'T' else 0 for x in S]

    ans = 0

    for i in range(len(S)):
        sum = 0
        for j in range(i, len(S)):
            if S[j] != 1:
                break
            sum += 1
        ans = max(ans, sum)
    print(ans)

if __name__ == "__main__":
    main()