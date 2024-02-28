import sys
input = sys.stdin.readline

def main(): 
    n = int(input())
    A = list(map(int, input().split(' ')))
    
    ans = 0
    for a in A:
        ans += a
        if ans < 0:
            ans = 0
    print(ans)        

if __name__ == "__main__":
    main()