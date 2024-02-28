import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    convert_dict = {}
    
    N = int(input())
    S = input().strip()
    Q = int(input())

    for i in range(26):
        convert_dict[chr(97+i)] = chr(97+i)
    
    for i in range(Q):
        c, d = map(str, input().split())
        for k, v in convert_dict.items():
            if v == c:
                convert_dict[k] = d

    
    ans = ""
    for i in range(N):
        if S[i] in convert_dict:
            ans += convert_dict[S[i]]
        else:
            ans += S[i]
    print(ans)
    
if __name__ == "__main__":
    main()