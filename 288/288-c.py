import sys
input = sys.stdin.readline

from collections import defaultdict, deque
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

que_closed = defaultdict(set)
ans = 0

def solve(s):
    count = 0
    que = deque()
    que.append(s)
    S = {s}
    while que:
        v = que.popleft()
        for i in graph[v]:
                que_closed[i].add(v)
                #print("({}, {})".format(v, i))
                if not i in S:
                    que.append(i)
                    S.add(i)
                else:
                    if i not in que_closed[v]:
                        count += 1
    return S, count

s = 1
left_node = set(range(1, n+1))
while len(left_node) != 0:
    S, count = solve(left_node.pop())

    ans += count
    left_node -= S

                #print(que_closed)
print(ans)