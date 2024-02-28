import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    S = input().rstrip()
    N = int(input())
    
    len_S = len(S)
    output = 0
    
    # calc input
    for i, s in enumerate(S):
        if s == "1":
            output += 1<<(len_S-i-1)
            if check_over(output, N):
                return 
    
    # calc output
    for i, s in enumerate(S):
        n = len_S-i-1
        
        if s == "?":
            output += check_under(output, n, N)

    print(output)

def check_over(inp, N):
    if inp > N:
        print(-1)
        return 1
    else:
        return 0
    
def check_under(out, n, N):
    if out + (1<<n) <= N:
        return 1<<n
    else:
        return 0




if __name__ == '__main__':
    main()


