import sys
input = sys.stdin.readline

def main():
    s = "1"
    n = int(input())

    for i in range(2, n+1):
        s = s + f" {i} " + s
    
    print(s)

if __name__ == "__main__":
    main()
