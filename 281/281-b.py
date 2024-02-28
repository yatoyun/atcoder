import sys
input = sys.stdin.readline

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

S = input().rstrip()

if len(S) != 8:
    print("No")
    exit()

if S[0].isupper() and S[0].isalpha() and S[-1].isupper() and S[-1].isalpha():
    if is_integer(S[1:-1]):
        x = int(S[1:-1])
        if x >= 100000 and x <= 999999:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")