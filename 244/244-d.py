import sys
input = sys.stdin.readline

def main():
    inp = input().split()
    ans = input().split()

    if inp == ans:
        print("Yes")
        exit()

    count = 0
    for i in range(3):
        if inp[i] == ans[i]:
            count += 1
    if count == 1:
        print("No")
    elif count == 0:
        print("Yes")

if __name__ == "__main__":
    main()