import sys
input = sys.stdin.readline

def main():
    S = input()
    T = ""
    S = sorted(S)
    for s in S:
        T += s
    print(T)
if __name__ == "__main__":
    main()