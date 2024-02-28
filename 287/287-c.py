import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(200000)
N, M = map(int, input().split())

glaph = defaultdict(list)



def run(u,ex_u, went_set):
    v = glaph[u]
    if len(v) == 1:
        return 0
    for next_v in v:
        if next_v != ex_u:
            if next_v in went_set:
                print("No")
                exit()
            ex_u = u
            went_set.add(next_v)
            return run(next_v,ex_u, went_set)

for _ in range(M):
    u, v = map(int, input().split())
    glaph[u].append(v)
    glaph[v].append(u)

    if len(glaph[u]) > 2 or len(glaph[v]) > 2:
        print("No")
        exit()

v_list = glaph[1]
if len(v_list) == 2:
    a,b = v_list
    went_set = {1, v_list[0], v_list[1]}
    run(v_list[0], 1, went_set)
    run(v_list[1], 1, went_set)
elif len(v_list) == 1:
    went_set = {1, v_list[0]}
    run(v_list[0], 1, went_set)
else:
    print("No")
    exit()

if len(went_set) == N:
    print("Yes")
else:
    print("No")
# u = 1
# ex_u = 0
# while True:
#     v = glaph[u]

#     if len(v) == 1:
#         break
#     else:
#         for next_v in v:
#             if next_v != ex_u:
#                 u = next_v
#                 ex_u = u
#                 break


# for i in range(M):
#     v = glaph[u]

#     for next_v in v:
#         if next_v != ex_u:
#             u = next_v
#             ex_u = u
#             break
#     if len(v) != 2:
#         break
# if i == M-1:
#     print("Yes")
# else:
#     print("No")
