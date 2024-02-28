import sys
input = sys.stdin.readline

def main():
    S = input().strip()
    s_set = list(set(S))

    if S.count(s_set[0]) > S.count(s_set[1]):
        small = s_set[1]
    else:
        small = s_set[0]
    
    print(S.find(small)+1)

if __name__ == "__main__":
    main()