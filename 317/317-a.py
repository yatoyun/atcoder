import sys
input = sys.stdin.readline

def main():
    N, H, X = map(int, input().split())
    P = list(map(int, input().split()))
    
    need_hp = X-H
    
    for i, p in enumerate(P):
        if p >= need_hp:
            print(i+1)
            return

if __name__ == "__main__":
    main()