from collections import Counter
input()
A = Counter(input().split())
B = Counter(input().split())
print("No" if B - A else "Yes")