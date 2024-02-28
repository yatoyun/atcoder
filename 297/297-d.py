import sys
input = sys.stdin.readline


A, B = map(int, input().split())
count = 0
while A != B:
	if A < B:
		A, B = B, A
	x = A // B
	A -= B * x
	count += x
	if A == 0:
		count -= 1
		break
print(count)
