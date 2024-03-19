import sys
input = sys.stdin.readline

S = input().rstrip()

ans = 0
ex_number = False
for s in S:
    if s != "0":
        ans += 1
        ex_number = False
    elif s=="0":
        if ex_number:
            ex_number = False
        else:
            ans += 1
            ex_number = True
    #print(ans)
print(ans)
