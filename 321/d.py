import sys
from bisect import bisect_right
input = sys.stdin.readline

def main():
    N, M, P = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    
    sum_list = [B[0]]
    for i in range(1,M):
        sum_list.append(B[i]+sum_list[-1])

    ans = 0
    for a in A:
        max_index = bisect_right(B, P-a) - 1
        if max_index < 0:
            ans += P * M
        else:
            ans += a*(max_index+1) + sum_list[max_index] + P * (M-(max_index+1))

    print(ans)
    

if __name__ == "__main__":
    main()