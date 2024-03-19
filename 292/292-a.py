import sys
input = sys.stdin.readline

S =   input().rstrip()

out = ""

for s in S:
    out += s.upper()

print(out)