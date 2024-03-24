import sys
input = sys.stdin.readline

def main():
    S = "wbwbwwbwbwbw"
    W, B = map(int, input().split())
    
    if W+B < len(S):
        S = S*2
        for i in range(len(S)):
            for j in range(i, len(S)):
                temp = S[i:j+1]
                temp.count("w")
                temp.count("b")
                if temp.count("w") == W and temp.count("b") == B:
                    print("Yes")
                    return
    else:
        S = (W+B)//len(S)*2*S
        for i in range(len(S)):
            for j in range(i, len(S)):
                temp = S[i:j+1]
                temp.count("w")
                temp.count("b")
                if temp.count("w") == W and temp.count("b") == B:
                    print("Yes")
                    return
    print("No")

if __name__ == "__main__":
    main()