import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    N = int(input())
    S = input().strip()
    
    alphabet_dict = defaultdict(int)
    
    cnt = 0
    start_char = S[0]
    for i in range(N):
        
        if S[i] != start_char:
            cnt = 0
            start_char = S[i]
        cnt += 1
        alphabet_dict[start_char] = max(cnt, alphabet_dict[start_char])
    cnt = 0
    for _, v in alphabet_dict.items():
        cnt += v
    
    print(cnt)
        
if __name__ == "__main__":
    main()