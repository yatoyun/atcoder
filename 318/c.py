import sys
input = sys.stdin.readline

def main():
    N, D, P = map(int, input().split())
    F = list(map(int, input().split()))
    F.sort()
    
    max_set = N // D+1
    ans = float('inf')
    sum_list = [F[0]]
    for i in range(1,N):
        sum_list.append(sum_list[-1] + F[i])
    
    for i in range(max_set+1):
        use_day = i * D
        total = i * P
        if use_day >= N:
            ans = min(ans, total)
            break
        total += sum_list[-use_day-1]
        ans = min(ans, total)
    print(ans)

if __name__ == "__main__":
    main()