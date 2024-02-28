import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    ex = A[0]
    for a in A[1:]:
        print(ex, end=' ')
        if abs(ex - a) != 1:
            not_abs(ex, a)
        ex = a
    
    print(A[-1])
    
def not_abs(a1, a2):
    if a1 < a2:
        for i in range(a1+1, a2):
            print(i, end=' ')
    else:
        for i in range(a1-1, a2, -1):
            print(i, end=' ')




if __name__ == '__main__':
    main()


