import sys
input = sys.stdin.readline

def calc_x(L, R, a):
    if L <= a <= R:
        return a
    elif a < L:
        return L
    else:
        return R

def main():
    N, L, R = map(int, input().split())
    
    A = list(map(int, input().split()))
    
    for a in A:
        print(calc_x(L, R, a), end=" ")

if __name__ == "__main__":
    main()