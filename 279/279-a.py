import sys
input = sys.stdin.readline

S = input()

output = 0

for s in S:
    if s == "v":
        output += 1
    elif s == "w":
        output += 2

print(output)