import sys
from collections import defaultdict
input = sys.stdin.readline

S = input().rstrip()

dict = defaultdict(str)

left_curve_number = 0
out = False
for i, s in enumerate(S):
    if s == "(":
        out = True
        left_curve_number += 1
    elif s == ")":
        dict[left_curve_number] = ""
        left_curve_number -= 1
    else:
        if s in dict.values():
            print("No")
            exit()
        dict[left_curve_number] += s
if not out:
    print("No")
else:
    print("Yes")
