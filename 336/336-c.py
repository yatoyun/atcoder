import sys
input = sys.stdin.readline

def main():
    N = int(input())
    convert_dict = {0:0, 1:2, 2:4, 3:6, 4:8}
    
    N -= 1
    if N == 0:
        print(0)
        return
    
    ans = ""
    while N:
        ans += str(convert_dict[N%5])
        N //= 5
    
    print(ans[::-1])

if __name__ == "__main__":
    main()