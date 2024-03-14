import sys
input = sys.stdin.readline

def main():
    ans = []
    n = int(input())
    ans.append(n)
    while n != 0:
        n = int(input())
        ans.append(n)
    
    for a in ans[::-1]:
        print(a)
    
if __name__ == "__main__":
    main()