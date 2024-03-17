import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    S = input().strip()

    logo_ans = 0
    amount = M
    logo_amount = 0
    for s in S:
        if s == "0":
            if logo_ans < logo_amount:
                logo_ans = logo_amount
                
            amount = M
            logo_amount = 0
        elif s == "1":
            if amount > 0:
                amount -= 1
            else:
                logo_amount += 1
        else:
            logo_amount += 1
    
    print(max(logo_ans, logo_amount))

if __name__ == "__main__":
    main()