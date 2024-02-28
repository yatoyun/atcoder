import sys
input = sys.stdin.readline


def main():
    N = int(input())
    
    a,b,c = 1, 1, 1
    for i in range(N-1):
        if b > c:
            c+=1
        elif a > b:
            b+=1
            c=1
        else:
            a+=1
            b=1
            c=1
    print(int('1'*a) + int('1'*b) + int('1'*c))

if __name__ == "__main__":
    main()