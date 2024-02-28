import sys
input = sys.stdin.readline

def main():
    s = []
    t = []
    n = int(input())
    for _ in range(n):
        u, v = input().split()
        s.append(u)
        t.append(v)
    for i in range(n):
        count = 0
        for S in [s[i], t[i]]:
            c = 1
            for j in range(n):
                if i != j:
                    if S == s[j] or S == t[j]:
                        c = 0
                        break
            if c == 1:
                count = 1
        if count == 0:
            print("No")
            exit()
    
    print("Yes")
        


    
if __name__ == "__main__":
    main()