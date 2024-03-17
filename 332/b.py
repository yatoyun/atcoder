import sys
input = sys.stdin.readline

def main():
    K, G, M = map(int, input().split())
    
    G_amount = 0
    M_amount = 0
    for i in range(K):
        if G_amount == G:
            G_amount = 0
        elif M_amount == 0:
            M_amount += M
        else:
            if M_amount > G - G_amount:
                M_amount -= G - G_amount
                G_amount = G
            else:
                G_amount += M_amount
                M_amount = 0
    print(G_amount, M_amount)

if __name__ == "__main__":
    main()