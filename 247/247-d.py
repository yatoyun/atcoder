import sys
from collections import deque

input = sys.stdin.readline

def main():
    q = deque()
    num = deque()
    n = int(input())
    for _ in range(n):
        query = [int(x) for x in input().split()]
        sum = 0
        if query[0] == 1:
            q.append(query[1])
            num.append(query[2])
        elif query[0] == 2:
            i = 0
            while query[1] > 0 and len(num) > 0:
                a = num.popleft()
                if a > query[1]:
                    a -= query[1]
                    sum += query[1] * q[0]
                    query[1] = 0
                    num.appendleft(a)
                    break
                if a <= query[1]:
                    query[1] -= a
                    sum += a * q[0]
                    q.popleft()
            print(sum)
    
    

if __name__ == "__main__":
    main()