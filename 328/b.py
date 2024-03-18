import sys
input = sys.stdin.readline

def count(D, month):
    ans = 0
    if month <= D[month-1]:
        ans += 1
    if month * 10 + month <= D[month-1]:
        ans += 1
    print(ans)
    return ans


def check(month, day):
    D_digits = [int(d) for d in str(month)]
    day_digits = [int(d) for d in str(day)]
    if sum(D_digits) != D_digits[0]*len(D_digits):
        return False

    for digit in day_digits:
        if digit != D_digits[0]:
            return False    
    return True

def main():
    N = int(input())
    D = list(map(int, input().split()))
    
    ans = 0
    for month in range(1, N+1):
        for day in range(1, D[month-1]+1):
            if check(month, day):
                ans += 1
    print(ans)

if __name__ == "__main__":
    main()