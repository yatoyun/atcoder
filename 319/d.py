import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    L = list(map(int, input().split()))
    
    max_L = max(L)-1
    sum_L = sum(L) + N
    
    l = max_L
    r = sum_L
    while r-l > 1:
        m = (l+r)//2
        row = 1
        length = 0
        for i in range(N):
            length += L[i]+1
            if length > m+1:
                row += 1
                length = L[i]+1
            
        if row <= M:
            r = m
        else:
            l = m  
    print(r)  
    
    
    

if __name__ == "__main__":
    main()