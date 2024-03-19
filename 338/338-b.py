import sys
input = sys.stdin.readline

def main():
    alpha_dict = {}
    S = input().strip()
    for s in S:
        if s in alpha_dict:
            alpha_dict[s] += 1
        else:
            alpha_dict[s] = 1
    
    max_s = S[0]
    for k, v in alpha_dict.items():
        if alpha_dict[max_s] < v:
            max_s = k
        if alpha_dict[max_s] == v:
            if max_s > k:
                max_s = k
    print(max_s)

if __name__ == "__main__":
    main()
