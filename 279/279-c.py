import sys
import numpy as np
input = sys.stdin.readline

H, W = map(int, input().split())

S = []
for _ in range(H):
    S.append(list(input().strip()))

T = []
for _ in range(H):
    T.append(list(input().strip()))

S = np.array(S).T
T = np.array(T).T

new_S = []
new_T = []
for s_list,t_list in zip(S.tolist(),T.tolist()):
    new_S.append(str(s_list).replace(".", "0").replace("#", "1"))
    new_T.append(str(t_list).replace(".", "0").replace("#", "1"))

new_S.sort()
new_T.sort()

for s, t in zip(new_S, new_T):
    if s != t:
        print("No")
        exit()
print("Yes")