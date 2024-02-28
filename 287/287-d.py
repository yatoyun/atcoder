import sys
from collections import defaultdict
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

len_t = len(T)

pre_dict = defaultdict(bool)
end_dict = defaultdict(bool)

pre_dict[0] = True
end_dict[0] = True
for i in range(len_t):

    if not pre_dict[i]:
        pre_dict[i+1] = False
    else:

        if T[i] == "?" or S[i] == "?" or T[i] == S[i]:
            pre_dict[i+1] = True
        else:
            pre_dict[i+1] = False

    if not end_dict[i]:
        end_dict[i+1] = False
    else:
        if T[-(i+1)] == "?" or S[-(i+1)] == "?" or T[-(i+1)] == S[-(i+1)]:
            end_dict[i+1] = True
        else:
            end_dict[i+1] = False

for i in range(len(T)+1):
    if pre_dict[i] and end_dict[len(T) - i]:
        print("Yes")
    else:
        print("No")
