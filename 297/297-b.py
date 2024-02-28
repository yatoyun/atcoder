import sys
input = sys.stdin.readline

S = input().rstrip()

B_indexs = []
R_indexs = []
K_indexs = 0
for i,s in enumerate(S):
	if s == "B":
		B_indexs.append(i)

	if s == "R":
		R_indexs.append(i)
	if s == "K":
		K_indexs = i

if B_indexs[0] % 2  == B_indexs[1] % 2:
	print("No")
	exit()

if not (R_indexs[0] < K_indexs and K_indexs < R_indexs[1]):
	print("No")
	exit()
print("Yes")
