import sys
input = sys.stdin.readline

def main():
    S = input().strip()
    ans = ""
    flag = True
    for s in S:
        if s == "|" and flag:
            flag = False
        elif s == "|" and not flag:
            flag = True
            continue
        
        if flag:
            ans += s
    
    print(ans)

if __name__ == "__main__":
    main()