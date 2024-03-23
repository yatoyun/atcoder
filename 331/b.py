import sys
input = sys.stdin.readline

def main():
    N, S, M, L = map(int, input().split())
    
    ans = float('inf')
    for i in range(N//6+2):
        for j in range(N//8+2):
            for k in range(N//12+2):
                if 6*i + 8*j + 12*k >= N:
                    ans = min(ans, (i*S+j*M+k*L))
    
    print(ans)

if __name__ == "__main__":
    main()