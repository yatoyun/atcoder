import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int, input().split()))

order = [a for a in range(1, N+1)]

ex_a = -1
most_ex_a = -1
for a in A:
    #print(*order)
    if a == ex_a+1:
        order.insert(most_ex_a-1, order.pop(a))

    else:
        order[a-1], order[a] = order[a], order[a-1]
        most_ex_a = a
    ex_a = a

print(*order)