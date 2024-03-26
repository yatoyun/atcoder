import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    N = int(input())
    str_dict = defaultdict(int)
    
    for _ in range(N):
        s = sorted(list(input().strip()))
        s = "".join(s)
        str_dict[s] += 1
    
    ans = 0
    for v in str_dict.values():
        if v > 1:
            ans += v * (v - 1) // 2
    
    print(ans)

if __name__ == "__main__":
    main()
