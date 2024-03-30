import sys
input = sys.stdin.readline

def main():
    N = int(input())
    S = list(input().strip())
    Q = int(input())
    
    is_capitalized = 0 # 0: original, 1: capitalized, 2: lower
    escaped_indexes = set()
    for _ in range(Q):
        t, x, c = input().split()
        t = int(t)
        x = int(x)
        if t == 1:
            S[x-1] = c
            escaped_indexes.add(x-1)
        elif t == 2:
            is_capitalized = 2
            escaped_indexes = set()
        else:
            is_capitalized = 1
            escaped_indexes = set()
    
    if is_capitalized == 0:
        print("".join(S))
        return

    for i, s in enumerate(S):
        if i in escaped_indexes:
            continue
        elif is_capitalized == 1:
            S[i] = s.upper()
        elif is_capitalized == 2:
            S[i] = s.lower()
    print("".join(S))
    
            
    

if __name__ == "__main__":
    main()