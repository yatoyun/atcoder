import sys
input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    S = input().strip()
    
    disjoint_indexes = [0]*N
    ex_str = S[0]
    for i in range(1, N):
        disjoint_indexes[i] = disjoint_indexes[i-1]
        if ex_str == S[i]:
            disjoint_indexes[i] += 1
        
        ex_str = S[i]
            
    for _ in range(Q):
        l, r = map(int, input().split())
        cnt = disjoint_indexes[r-1] - disjoint_indexes[l-1]
        
        print(cnt)

if __name__ == "__main__":
    main()